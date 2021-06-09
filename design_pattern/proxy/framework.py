from __future__ import annotations
from typing import List
from abc import ABC, abstractmethod


class RealObject(ABC):
	"""
	This class represents a real object in the proxy design pattern.
	"""

	@abstractmethod
	def get_list(self) -> List:
		raise NotImplementedError()


class ProxyObject(ABC):
	"""
	This class represents a proxy object in the proxy design pattern.
	"""

	@abstractmethod
	def get_list(self) -> List:
		raise NotImplementedError()
