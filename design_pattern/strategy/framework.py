from __future__ import annotations
from abc import ABC, abstractmethod


class Strategy(ABC):

	pass


class StrategyImplementor(ABC):

	@abstractmethod
	def perform_action(self, *, strategy: Strategy):
		raise NotImplementedError()
