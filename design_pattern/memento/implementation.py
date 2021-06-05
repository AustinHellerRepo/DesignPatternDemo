from __future__ import annotations
from design_pattern.memento.framework import Originator, Memento, Caretaker
from typing import List
from abc import ABC, abstractmethod


class Implementor(ABC):

	def __init__(self):

		self.__grocery_list = GroceryList(
			title="Untitled"
		)
		self.__grocery_list_history = Caretaker()

	def _save_history(func):
		def wrapper(self: Implementor, *args, **kwargs):
			_state = self.__grocery_list.get_state()
			self.__grocery_list_history.push(
				state=_state
			)
			return func(self, *args, **kwargs)
		return wrapper

	def undo(self):
		_is_successful, _grocery_list_state = self.__grocery_list_history.try_pop()
		if _is_successful:
			self.__grocery_list.set_state(
				state=_grocery_list_state
			)

	@_save_history
	def set_title(self, *, title: str):
		self.__grocery_list.set_title(
			title=title
		)

	@_save_history
	def add_item(self, *, item: str):
		self.__grocery_list.add_item(
			item=item
		)

	def get_title(self) -> str:
		return self.__grocery_list.get_title()

	def get_items(self) -> List[str]:
		return self.__grocery_list.get_items().copy()

	@abstractmethod
	def show(self):
		"""
		Provides an interface for the grocery list
		"""
		raise NotImplementedError()


class GroceryList(Originator):

	def __init__(self, *, title: str):

		self.__title = title
		self.__items = []  # type: List[str]

	def set_title(self, *, title: str):
		self.__title = title

	def get_title(self) -> str:
		return self.__title

	def add_item(self, *, item: str):
		self.__items.append(item)

	def get_items(self) -> List[str]:
		return self.__items.copy()

	def get_state(self) -> GroceryListState:
		return GroceryListState(
			title=self.__title,
			items=self.__items.copy()
		)

	def set_state(self, *, state: GroceryListState):
		self.__title = state.get_title()
		self.__items = state.get_items()


class GroceryListState(Memento):

	def __init__(self, *, title: str, items: List[str]):

		self.__title = title
		self.__items = items

	def get_title(self) -> str:
		return self.__title

	def get_items(self) -> List[str]:
		return self.__items
