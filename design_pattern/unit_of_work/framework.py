from __future__ import annotations
from abc import ABC, abstractmethod


class UnitOfWork(ABC):
	"""
	This class represents a unit of work to have a transaction started, data added to the object, the changes committed
		or rolled back without being committed.
	"""

	@abstractmethod
	def begin_transaction(self):
		raise NotImplementedError()

	@abstractmethod
	def commit(self) -> bool:
		raise NotImplementedError

	@abstractmethod
	def rollback(self):
		raise NotImplementedError()
