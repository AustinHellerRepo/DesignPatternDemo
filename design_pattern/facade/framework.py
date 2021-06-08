from __future__ import annotations
from typing import List
from abc import ABC, abstractmethod


class FacadeInterface(ABC):
	"""
	This class will facilitate the task of wrapping more complex actions into a simple function.
	"""

	def __init__(self, *, first_complex_class: FirstComplexClass, second_complex_class: SecondComplexClass, third_complex_class: ThirdComplexClass):

		self._first_complex_class = first_complex_class
		self._second_complex_class = second_complex_class
		self._third_complex_class = third_complex_class

	@abstractmethod
	def get_text_to_number(self, *, text: str) -> int:
		raise NotImplementedError()


class FirstComplexClass(ABC):
	"""
	This is a "complex" class that may be too complicated for some developers to use easily.
	"""

	@abstractmethod
	def format_text(self, *, text: str) -> str:
		raise NotImplementedError()


class SecondComplexClass(ABC):
	"""
	This is a "complex" class that may be too complicated for some developers to use easily.
	"""

	@abstractmethod
	def convert_text_to_list(self, *, text: str) -> List:
		raise NotImplementedError()


class ThirdComplexClass(ABC):
	"""
	This is a "complex" class that may be too complicated for some developers to use easily.
	"""

	@abstractmethod
	def get_number_of_elements_in_list(self, *, list_of_elements: List) -> int:
		raise NotImplementedError()
