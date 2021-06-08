from design_pattern.facade.framework import FacadeInterface, FirstComplexClass, SecondComplexClass, ThirdComplexClass
from typing import List


class ListElementCounter(FacadeInterface):
	"""
	This class demonstrates how three complex classes can be reduced to simple function calls
	"""

	def __init__(self, *, text_formatter: FirstComplexClass, text_to_list: SecondComplexClass, list_to_number: ThirdComplexClass):
		"""
		Load the facade via dependency injection
		"""

		super().__init__(
			first_complex_class=text_formatter,
			second_complex_class=text_to_list,
			third_complex_class=list_to_number
		)

		pass

	def get_text_to_number(self, *, text: str) -> int:
		"""
		This is the simplified interaction that the more complex classes produce separately.
		"""

		_formatted_text = self._first_complex_class.format_text(
			text=text
		)
		_list_of_characters = self._second_complex_class.convert_text_to_list(
			text=_formatted_text
		)
		_number_of_elements = self._third_complex_class.get_number_of_elements_in_list(
			list_of_elements=_list_of_characters
		)
		return _number_of_elements


class AddHyphensToString(FirstComplexClass):
	"""
	This class performs some "complex" string task.
	"""

	def format_text(self, *, text: str) -> str:
		_formatted_text = ""
		for _character_index, _character in enumerate(text):
			if _character_index != 0:
				_formatted_text += "-"
			_formatted_text += _character
		return _formatted_text


class ConvertTextToListOfLetters(SecondComplexClass):
	"""
	This class performs some "complex" conversion task.
	"""

	def convert_text_to_list(self, *, text: str) -> List:
		_list_of_letters = []
		for _character in text:
			_list_of_letters.append(_character)
		return _list_of_letters


class GetNumberOfElementsInList(ThirdComplexClass):
	"""
	This class performs some "complex" reduction task.
	"""

	def get_number_of_elements_in_list(self, *, list_of_elements: List) -> int:
		return len(list_of_elements)
