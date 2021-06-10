from __future__ import annotations
from abc import ABC, abstractmethod


class Visitor(ABC):
	"""
	This class represents the visitor that can perform the actions of the supported visitor elements.
	"""

	@abstractmethod
	def perform_first_visitor_element_action(self, *, first_visitor_element: FirstVisitorElement):
		raise NotImplementedError()

	@abstractmethod
	def perform_second_visitor_element_action(self, *, second_visitor_element: SecondVisitorElement):
		raise NotImplementedError()


class VisitorElement(ABC):
	"""
	This class is the base class for being a visitor element.
	"""

	@abstractmethod
	def perform_action(self, *, visitor: Visitor):
		raise NotImplementedError()


class FirstVisitorElement(VisitorElement):
	"""
	This class is one of the two logical divisions of the supported visitor elements.
	"""

	def perform_action(self, *, visitor: Visitor):
		visitor.perform_first_visitor_element_action(
			first_visitor_element=self
		)

	@abstractmethod
	def first_visitor_element_action(self):
		raise NotImplementedError()


class SecondVisitorElement(VisitorElement):
	"""
	This class is one of the two logical divisions of the supported visitor elements.
	"""

	def perform_action(self, *, visitor: Visitor):
		visitor.perform_second_visitor_element_action(
			second_visitor_element=self
		)

	@abstractmethod
	def second_visitor_element_action(self):
		raise NotImplementedError()
