from __future__ import annotations
from design_pattern.unit_of_work.framework import UnitOfWork
from typing import List


class ConsoleUnitOfWork(UnitOfWork):
	"""
	This class implements the unit of work class.
	"""

	def __init__(self):

		self.__is_transaction_started = False
		self.__console_output_lines = []  # type: List[str]

	def begin_transaction(self):
		"""
		This function ensures that the instance is ready to store data for the transaction.
		"""

		if self.__is_transaction_started:
			raise Exception(f"Transaction already started")
		self.__is_transaction_started = True

	def add_console_output(self, *, text: str):
		"""
		This function stores text until it is committed later.
		"""

		if not self.__is_transaction_started:
			raise Exception(f"Transaction not started")
		self.__console_output_lines.append(text)

	def commit(self) -> bool:
		"""
		This function commits all stored text such that it is all printed to the console and ends the transaction.
		"""

		if not self.__is_transaction_started:
			raise Exception(f"Transaction not started")
		for _console_output_line in self.__console_output_lines:
			print(_console_output_line)
		self.__console_output_lines.clear()
		self.__is_transaction_started = False
		return True

	def rollback(self):
		"""
		This function rolls back all added text and ends the transaction.
		"""

		if not self.__is_transaction_started:
			raise Exception(f"Transaction not started")
		self.__console_output_lines.clear()
		self.__is_transaction_started = False
