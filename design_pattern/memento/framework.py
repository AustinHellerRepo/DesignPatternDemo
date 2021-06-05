from __future__ import annotations
from typing import List, Tuple
from abc import ABC, abstractmethod


class Originator(ABC):
	"""
	This class contains a state that can change.
	"""

	@abstractmethod
	def get_state(self) -> Memento:
		raise NotImplementedError()

	@abstractmethod
	def set_state(self, *, state: Memento):
		raise NotImplementedError()


class Memento(ABC):
	"""
	This class represents a state of the originator
	"""


class Caretaker():
	"""
	This class maintains a history of states as provided by the originator
	"""

	def __init__(self):

		self.__states = []  # type: List[Memento]

	def push(self, *, state: Memento):
		self.__states.append(state)

	def try_pop(self) -> Tuple[bool, Memento]:
		if len(self.__states) == 0:
			return False, None
		else:
			return True, self.__states.pop()
