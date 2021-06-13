from __future__ import annotations
from design_pattern.repository.framework import Repository, DatabaseInterface
from typing import Dict, List
from datetime import datetime
import json
from abc import ABC, abstractmethod


class MemoryDatabaseInterface(DatabaseInterface):
	"""
	This is an in-memory database interface to allow me to demonstrate the Repository design pattern.
	"""

	def __init__(self):
		super().__init__(
			database_connection=None
		)

		self.__last_table_entry_id_by_table_name = {}  # type: Dict[str, int]
		self.__table_entry_per_table_entry_id_per_table_name = {}  # type: Dict[str, Dict[int, Dict]]

	def execute_query(self, *, query: str, parameters: Dict[str, str or int]) -> List[Dict] or None:
		"""
		This function does basic string parsing to determine which operation needs to occur.
		:param query: one of the basic operations ("SELECT", "INSERT", "UPDATE", "DELETE", or "CREATE" to create the table) followed by the table name
		:param parameters: the necessary parameters for the provided query
		:return: a list of dictionaries of the raw database rows returned by the provided query, if applicable
		"""

		if query is None or len(query.split(' ')) != 2:
			raise Exception(f"Unexpected query format: \"{query}\".")
		_function = query.split(' ')[0]
		_table_name = query.split(' ')[1]
		if _function == "SELECT":

			# this would normally involve a SELECT statement to run against a real database_interface

			if _table_name not in self.__table_entry_per_table_entry_id_per_table_name.keys():
				raise MemoryDatabaseInterfaceException(f"Table does not exist: \"{_table_name}\".")
			_id = parameters["id"]
			_rows = []  # type: List[Dict]
			if _id is None:
				# return all rows
				for _id in self.__table_entry_per_table_entry_id_per_table_name[_table_name]:
					_row = self.__table_entry_per_table_entry_id_per_table_name[_table_name][_id]
					_rows.append(_row)
			else:
				if _id not in self.__table_entry_per_table_entry_id_per_table_name[_table_name].keys():
					raise IdNotFoundException(f"Row does not exist in {_table_name} with id: {_id}")
				_row = self.__table_entry_per_table_entry_id_per_table_name[_table_name][_id]
				_rows.append(_row)
			return _rows
		elif _function == "INSERT":

			# this would normally involve an INSERT statement to run against a real database_interface

			if _table_name not in self.__table_entry_per_table_entry_id_per_table_name.keys():
				raise MemoryDatabaseInterfaceException(f"Table does not exist: \"{_table_name}\".")
			self.__last_table_entry_id_by_table_name[_table_name] += 1
			_id = self.__last_table_entry_id_by_table_name[_table_name]
			_row_create_datetime = datetime.utcnow()
			_row_update_datetime = _row_create_datetime
			_row = parameters.copy()
			if "id" in _row.keys():
				raise MemoryDatabaseInterfaceException("Parameters cannot contain \"id\".")
			if "row_create_datetime" in _row.keys():
				raise MemoryDatabaseInterfaceException(f"Parameters cannot contain \"row_create_datetime\".")
			if "row_update_datetime" in _row.keys():
				raise MemoryDatabaseInterfaceException(f"Parameters cannot contain \"row_update_datetime\".")
			_row["id"] = _id
			_row["row_create_datetime"] = _row_create_datetime
			_row["row_update_datetime"] = _row_update_datetime
			self.__table_entry_per_table_entry_id_per_table_name[_table_name][_id] = _row
			return [_row]
		elif _function == "UPDATE":

			# this would normally involve an UPDATE statement to run against a real database_interface

			if _table_name not in self.__table_entry_per_table_entry_id_per_table_name.keys():
				raise MemoryDatabaseInterfaceException(f"Table does not exist: \"{_table_name}\".")
			_updated_row = parameters.copy()
			if "id" not in _updated_row.keys():
				raise MemoryDatabaseInterfaceException("Missing \"id\" key in UPDATE parameters.")
			if "row_create_datetime" in _updated_row.keys():
				raise MemoryDatabaseInterfaceException(f"Parameters cannot contain \"row_create_datetime\".")
			if "row_update_datetime" in _updated_row.keys():
				raise MemoryDatabaseInterfaceException(f"Parameters cannot contain \"row_update_datetime\".")
			_id = _updated_row["id"]
			if _id not in self.__table_entry_per_table_entry_id_per_table_name[_table_name].keys():
				raise IdNotFoundException(f"Row does not exist in table \"{_table_name}\" with id: {_id}")
			_current_row = self.__table_entry_per_table_entry_id_per_table_name[_table_name][_id]
			_row_create_datetime = _current_row["row_create_datetime"]
			_updated_row["row_create_datetime"] = _row_create_datetime
			_updated_row["row_update_datetime"] = datetime.utcnow()
			self.__table_entry_per_table_entry_id_per_table_name[_table_name][_id] = _updated_row
			return [_updated_row]
		elif _function == "DELETE":

			# this would normally involve a DELETE statement to run against a real database_interface

			if _table_name not in self.__table_entry_per_table_entry_id_per_table_name.keys():
				raise MemoryDatabaseInterfaceException(f"Table does not exist: \"{_table_name}\".")
			if "id" not in parameters.keys():
				raise MemoryDatabaseInterfaceException("Missing \"id\" key in DELETE parameters.")
			_id = parameters["id"]
			_rows = []  # type: List[Dict]
			if _id is None:
				# delete all rows
				for _id in self.__table_entry_per_table_entry_id_per_table_name[_table_name]:
					_row = self.__table_entry_per_table_entry_id_per_table_name[_table_name][_id]
					_rows.append(_row)
				self.__table_entry_per_table_entry_id_per_table_name[_table_name].clear()
			else:
				if _id not in self.__table_entry_per_table_entry_id_per_table_name[_table_name].keys():
					raise IdNotFoundException(f"Row does not exist in \"{_table_name}\" with id: {_id}")
				_row = self.__table_entry_per_table_entry_id_per_table_name[_table_name][_id]
				del self.__table_entry_per_table_entry_id_per_table_name[_table_name][_id]
			return _rows
		elif _function == "CREATE":

			# this would normally involve a CREATE TABLE statement to run against a real database_interface

			if _table_name not in self.__last_table_entry_id_by_table_name.keys():
				self.__last_table_entry_id_by_table_name[_table_name] = 0
				self.__table_entry_per_table_entry_id_per_table_name[_table_name] = {}  # type: Dict[int, Dict]
		else:
			raise MemoryDatabaseInterfaceException(f"Unexpected function call to database: \"{_function}\".")


class MemoryDatabaseInterfaceException(Exception):
	"""
	This class represents any exception thrown by the MemoryDatabaseInterface class
	"""

	pass


class IdNotFoundException(MemoryDatabaseInterfaceException):
	"""
	This class represents an exception in finding the primary key id in the specified table
	"""

	pass


class RowObject(ABC):
	"""
	This class represents a parsed row object from the row dictionary provided by a database interface.
	"""

	@staticmethod
	@abstractmethod
	def parse_database_row(*, row_dict: Dict) -> RowObject:
		"""
		This function will parse out the details of the row dictionary and return the corresponding row object.
		:param row_dict: a dictionary containing the details of the row object
		:return: a row object containing details from the row dictionary
		"""
		raise NotImplementedError()

	def get_json(self) -> str:
		"""
		This function returns the json string of this row object.
		:return: a string containing the parsed json of this object
		"""
		def _default(o):
			if isinstance(o, datetime):
				return o.isoformat()
			else:
				return o.__dict__
		return json.dumps(self, default=_default, sort_keys=True, indent=4)


class User(RowObject):
	"""
	This class represents a user who can make orders.
	"""

	def __init__(self, *, user_id: int, name: str, create_datetime: datetime, update_datetime: datetime):

		self.user_id = user_id
		self.name = name
		self.create_datetime = create_datetime
		self.update_datetime = update_datetime

	@staticmethod
	def parse_database_row(*, row_dict: Dict) -> User:
		_user = User(
			user_id=row_dict["id"],
			name=row_dict["name"],
			create_datetime=row_dict["row_create_datetime"],
			update_datetime=row_dict["row_update_datetime"]
		)
		return _user


class UserRepository(Repository):
	"""
	This class implements the Repository class and provides a means to add/get/update/remove users.
	"""

	def __init__(self, *, database_interface: DatabaseInterface):
		super().__init__(
			database_interface=database_interface
		)

		# creates the user table if it does not already exist
		self._database_interface.execute_query(
			query="CREATE USER",
			parameters={}
		)

	def add(self, *, database_object_dict: Dict) -> User:
		"""
		This function adds a user to the table.
		:param database_object_dict: a dictionary containing the necessary user properties for the user table
		:return: an instance of user that was inserted into the table
		"""

		_row_dict_list = self._database_interface.execute_query(
			query=f"INSERT USER",
			parameters={
				"name": database_object_dict["name"]
			}
		)
		if len(_row_dict_list) != 1:
			raise RepositoryException(f"Unexpected number of rows added: {len(_row_dict_list)}")
		_user = User.parse_database_row(
			row_dict=_row_dict_list[0]
		)
		return _user

	def update(self, *, database_object: User) -> User:
		"""
		This function updates the user in the table to match the contents of the provided user object.
		:param database_object: The user to be updated in the database based on the internal user_id field
		:return: The updated user that is currently contained in the table
		"""

		_row_dict_list = self._database_interface.execute_query(
			query=f"UPDATE USER",
			parameters={
				"id": database_object.user_id,
				"name": database_object.name
			}
		)
		if len(_row_dict_list) != 1:
			raise RepositoryException(f"Unexpected number of rows updated: {len(_row_dict_list)}")
		_user = User.parse_database_row(
			row_dict=_row_dict_list[0]
		)
		return _user

	def get(self, *, database_object_id: int or None) -> List[User]:
		"""
		This function returns zero or more users based on the provided database object id. If None is provided, all records are returned.
		:param database_object_id: the user ID of the user to be returned or None if all users should be returned
		:return: One user if a user ID is provided or all users if None is provided
		"""

		_row_dict_list = self._database_interface.execute_query(
			query=f"SELECT USER",
			parameters={
				"id": database_object_id
			}
		)
		_users = []  # type: List[User]
		for _row_dict in _row_dict_list:
			_user = User.parse_database_row(
				row_dict=_row_dict
			)
			_users.append(_user)
		return _users

	def remove(self, *, database_object_id: int or None) -> List[User]:
		"""
		This function removes the specific user based on the provided user ID or all users if None is provided.
		:param database_object_id: the user ID to be removed or None if all users should be removed
		:return: the users that were removed
		"""

		# verify that none of the removed users are tied to an existing order
		_order_repository = OrderRepository(
			database_interface=self._database_interface
		)
		_orders = _order_repository.get(
			database_object_id=None
		)
		if database_object_id is None:
			if len(_orders) != 0:
				raise RepositoryException(f"Cannot clear out all users while orders still exist for those users.")
		else:
			for _order in _orders:
				if _order.user_id == database_object_id:
					raise RepositoryException(f"Cannot remove user with id {database_object_id} while order exists with id {_order.order_id}.")

		_row_dict_list = self._database_interface.execute_query(
			query=f"DELETE USER",
			parameters={
				"id": database_object_id
			}
		)
		_users = []  # type: List[User]
		for _row_dict in _row_dict_list:
			_user = User.parse_database_row(
				row_dict=_row_dict
			)
			_users.append(_user)
		return _users


class Order(RowObject):
	"""
	This class represents an order that a user has placed.
	"""

	def __init__(self, *, order_id: int, product: str, user_id: int, create_datetime: datetime, update_datetime: datetime):

		self.order_id = order_id
		self.product = product
		self.user_id = user_id
		self.create_datetime = create_datetime
		self.update_datetime = update_datetime

	@staticmethod
	def parse_database_row(*, row_dict: Dict) -> Order:
		_order = Order(
			order_id=row_dict["id"],
			product=row_dict["product"],
			user_id=row_dict["user_id"],
			create_datetime=row_dict["row_create_datetime"],
			update_datetime=row_dict["row_update_datetime"]
		)
		return _order


class OrderRepository(Repository):
	"""
	This class implements the Repository class and provides a means to add/get/update/remove orders.
	"""

	def __init__(self, *, database_interface: DatabaseInterface):
		super().__init__(
			database_interface=database_interface
		)

		# creates the order table if it does not already exist
		self._database_interface.execute_query(
			query="CREATE ORDER",
			parameters={}
		)

	def add(self, *, database_object_dict: Dict) -> Order:
		"""
		This function adds an order to the table.
		:param database_object_dict: a dictionary containing the necessary order properties for the order table
		:return: an instance of order that was inserted into the table
		"""

		# verify that user exists
		_user_repository = UserRepository(
			database_interface=self._database_interface
		)
		try:
			_user = _user_repository.get(
				database_object_id=database_object_dict["user_id"]
			)
		except IdNotFoundException as ex:
			raise RepositoryException(f"Cannot add order without first adding user with id: {database_object_dict['user_id']}")

		_row_dict_list = self._database_interface.execute_query(
			query=f"INSERT ORDER",
			parameters={
				"product": database_object_dict["product"],
				"user_id": database_object_dict["user_id"]
			}
		)
		if len(_row_dict_list) != 1:
			raise RepositoryException(f"Unexpected number of rows added: {len(_row_dict_list)}")
		_order = Order.parse_database_row(
			row_dict=_row_dict_list[0]
		)
		return _order

	def update(self, *, database_object: Order) -> Order:
		"""
		This function updates the order in the table to match the contents of the provided order object.
		:param database_object: The order to be updated in the database based on the internal order_id field
		:return: The updated order that is currently contained in the table
		"""

		# verify that user exists
		_user_repository = UserRepository(
			database_interface=self._database_interface
		)
		try:
			_user = _user_repository.get(
				database_object_id=database_object.user_id
			)
		except IdNotFoundException as ex:
			raise RepositoryException(f"Cannot add order without first adding user with id: {database_object.user_id}")

		_row_dict_list = self._database_interface.execute_query(
			query=f"UPDATE ORDER",
			parameters={
				"id": database_object.order_id,
				"product": database_object.product,
				"user_id": database_object.user_id
			}
		)
		if len(_row_dict_list) != 1:
			raise RepositoryException(f"Unexpected number of rows updated: {len(_row_dict_list)}")
		_order = Order.parse_database_row(
			row_dict=_row_dict_list[0]
		)
		return _order

	def get(self, *, database_object_id: int or None) -> List[Order]:
		"""
		This function returns zero or more orders based on the provided database object id. If None is provided, all records are returned.
		:param database_object_id: the order ID of the order to be returned or None if all orders should be returned
		:return: One order if an order ID is provided or all orders if None is provided
		"""

		_row_dict_list = self._database_interface.execute_query(
			query=f"SELECT ORDER",
			parameters={
				"id": database_object_id
			}
		)
		_orders = []  # type: List[Order]
		for _row_dict in _row_dict_list:
			_order = Order.parse_database_row(
				row_dict=_row_dict
			)
			_orders.append(_order)
		return _orders

	def remove(self, *, database_object_id: int or None) -> List[Order]:
		"""
		This function removes the specific order based on the provided order ID or all orders if None is provided.
		:param database_object_id: the order ID to be removed or None if all orders should be removed
		:return: the orders that were removed
		"""

		_row_dict_list = self._database_interface.execute_query(
			query=f"DELETE ORDER",
			parameters={
				"id": database_object_id
			}
		)
		_orders = []  # type: List[Order]
		for _row_dict in _row_dict_list:
			_order = Order.parse_database_row(
				row_dict=_row_dict
			)
			_orders.append(_order)
		return _orders


class RepositoryException(Exception):
	"""
	This class represents any exception thrown by the implementations of the Repository class.
	"""

	pass
