from design_pattern.proxy.framework import RealObject, ProxyObject
from typing import List
import time


class Television(RealObject):
	"""
	This class represents a television with a list of channels.
	"""

	def get_list(self) -> List:
		"""
		Returns the list of available channels
		"""

		print("Returning the full list of channels from the real television")

		# demonstrating a delay that would warrant caching this list
		time.sleep(3)

		return [
			"Channel 1",
			"Channel 2",
			"Channel 3"
		]


class CachedTelevision(ProxyObject):
	"""
	This class implements the proxy design pattern, demonstrating one benefit by caching the results of a function.
	"""

	def __init__(self):
		super().__init__()

		self.__cached_list = None  # type: List[str]

		# in a real project, I would have passed in a factory to create this instance
		self.__television = Television()

	def clear_cache(self):
		"""
		Clears the cached list of results so that the next attempt to get the list will pull a fresh copy
		"""

		self.__cached_list = None

		print("Cache cleared")

	def get_list(self) -> List:
		"""
		This returned a cached list of results from the television class
		"""

		if self.__cached_list is None:
			self.__cached_list = self.__television.get_list()
		else:
			print("Returning the cached list of channels from the proxy television")

		return self.__cached_list
