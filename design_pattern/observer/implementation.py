from __future__ import annotations
from design_pattern.observer.framework import Observer, Observable
from typing import List
from enum import Enum, auto


class RadioStation(Observable):
	"""
	This class sends out song updates to listening radios.
	"""

	def __init__(self, *, name: str):
		super().__init__()

		self.__name = name

	def get_name(self) -> str:
		return self.__name


class Radio(Observer):
	"""
	This class listens for notifications from nearby radio stations.
	"""

	def __init__(self, *, location: str):

		self.__location = location

	def receive_notification(self, *args, **kwargs):
		"""
		This is a basic implementation that assumes the format of the arguments.
		"""
		print(f"{self.__location} is now hearing \"{args[0]}\" on {args[1]}")
