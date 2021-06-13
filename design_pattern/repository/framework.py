from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, List


class Repository(ABC):
	"""
	This class represents a generic repository and its basic functions.
	"""

	def __init__(self, *, database_interface: DatabaseInterface):
		"""
		Initializes the repository instance
		:param database_interface: the object that provides direct access to the database
		"""

		self._database_interface = database_interface

	@abstractmethod
	def add(self, *, database_object_dict) -> object:
		"""
		Adds the provided dictionary of data to the table this repository pertains to.
		:param database_object_dict: a dictionary of data that will be parsed out and inserted into the database
		:return: the row object that includes any auto-incrementing IDs and auto-generated data (create datetime, etc.)
		"""
		raise NotImplementedError()

	@abstractmethod
	def update(self, *, database_object) -> object:
		"""
		Updates the database to match the state of the provided database row object.
		:param database_object: the row object that should be pushed to and updated in the database
		:return: the updated database row object that includes any on-update triggered columns
		"""
		raise NotImplementedError()

	@abstractmethod
	def get(self, *, database_object_id) -> List[object]:
		"""
		Returns the row objects that correspond to the provided database object ID or all rows if None is provided
		:param database_object_id: the primary key of the database object or None for all
		:return: the row objects that correspond to the provided database object ID or all rows
		"""
		raise NotImplementedError()

	@abstractmethod
	def remove(self, *, database_object_id) -> List[object]:
		"""
		Removes the database entries that correspond to the provided database object ID or all rows if None is provided
		:param database_object_id: the primary key of the entry to be removed or None if all should be cleared
		:return: the row objects that were removed from the database
		"""
		raise NotImplementedError()


class DatabaseInterface(ABC):
	"""
	This class is an abstract wrapper over the existing database connection.
	"""

	def __init__(self, *, database_connection):
		"""
		Initializes the generic database interface as a wrapper of the more complex database connection object.
		:param database_connection: the direct database object that permits query execution
		"""

		self._database_connection = database_connection

	@abstractmethod
	def execute_query(self, *, query: str, parameters: Dict[str, str or int]) -> List[Dict] or None:
		"""
		This function executes any arbitrary query and passes in the provided parameters.
		:param query: the query that will be executed on the database
		:param parameters: the parameters passed into the query
		:return: zero or more row objects, None if query does not return results (no SELECT statement)
		"""
		raise NotImplementedError()
