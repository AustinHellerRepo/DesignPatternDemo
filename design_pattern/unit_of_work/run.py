from design_pattern.unit_of_work.implementation import ConsoleUnitOfWork
from datetime import datetime


_datetime_format = "%Y-%m-%d %H:%M:%S.%f"
_console_unit_of_work = ConsoleUnitOfWork()

# start loop to allow user to test unit of work
_is_active = True
while _is_active:
	print("========================")
	print("Choose option from below")
	print("1: Begin transaction")
	print("2: Add text")
	print("3: Commit transaction")
	print("4: Rollback transaction")
	print("5: Exit")
	_user_input = input("Choice: ")
	if _user_input == "1":
		_console_unit_of_work.begin_transaction()
	elif _user_input == "2":
		_console_text = input("Text: ")
		_console_unit_of_work.add_console_output(
			text=f"{datetime.now().strftime(_datetime_format)}: {_console_text}"
		)
	elif _user_input == "3":
		_console_unit_of_work.commit()
	elif _user_input == "4":
		_console_unit_of_work.rollback()
	elif _user_input == "5":
		_is_active = False
	else:
		print(f"Unexpected user input: \"{_user_input}\".")
