from design_pattern.visitor.framework import FirstVisitorElement, SecondVisitorElement, Visitor


class TextFormatter(Visitor):
	"""
	This class formats the text provided by the visitor elements.
	"""

	def __init__(self, *, is_upper: bool):

		self.__is_upper = is_upper

	def perform_first_visitor_element_action(self, *, first_visitor_element: FirstVisitorElement):
		_text = first_visitor_element.first_visitor_element_action()  # type: str
		if self.__is_upper:
			_formatted_text = _text.upper()
		else:
			_formatted_text = _text.lower()
		print(f"Formatted text: \"{_formatted_text}\"")

	def perform_second_visitor_element_action(self, *, second_visitor_element: SecondVisitorElement):
		_text = second_visitor_element.second_visitor_element_action()  # type: str
		if self.__is_upper:
			_formatted_text = _text.upper()
		else:
			_formatted_text = _text.lower()
		print(f"Formatted text: \"{_formatted_text}\"")


class PoemSource(FirstVisitorElement):
	"""
	This class provides a poem to the visitor.
	"""

	def __init__(self, *, poem: str):

		self.__poem = poem

	def first_visitor_element_action(self):
		return self.__poem


class UserInputSource(SecondVisitorElement):
	"""
	This class provides raw user input to the visitor.
	"""

	def __init__(self, *, message: str):

		self.__message = message

	def second_visitor_element_action(self):
		_user_input = input(f"{self.__message}: ")
		return _user_input
