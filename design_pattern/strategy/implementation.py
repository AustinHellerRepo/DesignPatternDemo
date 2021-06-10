from design_pattern.strategy.framework import Strategy, StrategyImplementor


class TextFormatter(Strategy):
	"""
	This class contains the necessary information needed to accomplish the strategy.
	"""

	def __init__(self, *, is_upper: bool):

		self.__is_upper = is_upper

	def is_upper(self) -> bool:
		return self.__is_upper


class PoemSource(StrategyImplementor):
	"""
	This class provides a specific implementation of the provided strategy.
	"""

	def __init__(self, *, poem: str):

		self.__poem = poem

	def perform_action(self, *, strategy: TextFormatter):
		if strategy.is_upper():
			_formatted_text = self.__poem.upper()
		else:
			_formatted_text = self.__poem.lower()
		print(_formatted_text)


class UserInputSource(StrategyImplementor):
	"""
	This class provides a specific implementation of the provided strategy.
	"""

	def __init__(self, *, message: str):

		self.__message = message

	def perform_action(self, *, strategy: TextFormatter):
		_user_input = input(f"{self.__message}: ")
		if strategy.is_upper():
			_formatted_text = _user_input.upper()
		else:
			_formatted_text = _user_input.lower()
		print(_formatted_text)
