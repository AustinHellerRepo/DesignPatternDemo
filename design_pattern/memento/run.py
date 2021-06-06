from design_pattern.memento.implementation import Implementor
import os


class ConsoleDisplay(Implementor):
	"""
	This class implements the interface for the
	"""

	def __init__(self):
		super().__init__()

		pass

	def show(self):

		# gather all of the lines to be printed out
		_lines = []  # type: List[str]
		_lines.append(f"Title: {self.get_title()}")
		if len(self.get_items()) == 0:
			_lines.append("(no items)")
		else:
			for _item_index, _item in enumerate(self.get_items()):
				_lines.append(f"{_item_index + 1}. {_item}")

		# determine the max length in order to properly crop the output
		_max_length = 0
		for _line in _lines:
			if len(_line) > _max_length:
				_max_length = len(_line)

		# clear the screen
		if os.name == "nt":
			os.system("cls")
		else:
			os.system("clear")

		# display the output
		print("=" * _max_length)
		for _line in _lines:
			print(_line)
		print("=" * _max_length)


_console_display = ConsoleDisplay()

_is_active = True
while _is_active:
	print("Please make a choice from the options below")
	print("1: Set title")
	print("2: Add item")
	print("3: Show list")
	print("4: Undo")
	print("5: Exit")
	_user_input = input("Choice: ")
	if _user_input == "1":
		_title = input("Title: ").strip()
		if _title != "":
			_console_display.set_title(
				title=_title
			)
	elif _user_input == "2":
		_item = input("Item: ").strip()
		if _item != "":
			_console_display.add_item(
				item=_item
			)
	elif _user_input == "3":
		_console_display.show()
	elif _user_input == "4":
		_console_display.undo()
	elif _user_input == "5":
		_is_active = False
	else:
		print(f"Unexpected user input: \"{_user_input}\".")
