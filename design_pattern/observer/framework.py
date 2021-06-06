from __future__ import annotations
from typing import List
from abc import ABC, abstractmethod


class Observer(ABC):
	"""
	This class waits for notifications from observable objects.
	"""

	@abstractmethod
	def receive_notification(self, *args, **kwargs):
		"""
		This function is called by observables that this observer is registered with.
		"""
		raise NotImplementedError()


class Observable(ABC):
	"""
	This class emits notifications to registered observers.
	"""

	def __init__(self):

		self.__observers = []  # type: List[Observer]

	def add_observer(self, *, observer: Observer):
		"""
		This function registers the observer with this observable.
		"""
		self.__observers.append(observer)

	def notify_observers(self, *args, **kwargs):
		"""
		This function sends out a notification to all registered observables.
		"""
		for _observer in self.__observers:
			_observer.receive_notification(*args, **kwargs)
