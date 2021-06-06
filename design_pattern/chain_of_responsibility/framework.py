from __future__ import annotations
from typing import List
from abc import ABC, abstractmethod


class ChainLink(ABC):
	"""
	This class represents a link in a chain of processing steps.
	"""

	def __init__(self):

		self.__next_chain_link = None  # type: ChainLink

	@abstractmethod
	def process_chain_link(self, *args, **kwargs) -> object:
		"""
		This function is the unit of work that this chain link is designed to complete in the chain.
		"""
		raise NotImplementedError()

	def process_chain(self, *args, **kwargs) -> List[object]:
		"""
		This function processes all of the links in the chain, returning the list of objects from each chain link's process.
		"""
		_results = []  # type: List[object]
		_results.append(self.process_chain_link(*args, **kwargs))
		if self.__next_chain_link is not None:
			_results.extend(self.__next_chain_link.process_chain(*args, **kwargs))
		return _results

	def set_next(self, chain_link: ChainLink) -> ChainLink:
		"""
		Sets the next chain link to be evaluated after this instance.
		:param chain_link: the chain link to be added to the chain
		:return: the passed in chain link for convenience
		"""
		self.__next_chain_link = chain_link
		return chain_link
