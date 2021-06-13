from design_pattern.repository.implementation import MemoryDatabaseInterface, MemoryDatabaseInterfaceException, RepositoryException, UserRepository, User, OrderRepository, Order
from typing import List


# instantiate the database interface
_database_interface = MemoryDatabaseInterface()

# create the repositories
_user_repository = UserRepository(
	database_interface=_database_interface
)

_order_repository = OrderRepository(
	database_interface=_database_interface
)

# begin accepting user input
_is_active = True
while _is_active:
	print("===========================================")
	print("Please make a choice from the options below")
	print("1: Add user")
	print("2: Get user (empty = all)")
	print("3: Update user")
	print("4: Remove user (empty = all)")
	print("5: Add order")
	print("6: Get order (empty = all)")
	print("7: Update order")
	print("8: Remove order (empty = all)")
	print("9: Exit")
	_user_input = input("Choice: ")
	try:
		if _user_input == "1":  # add user
			_name = input("Name: ")
			_user = _user_repository.add(
				database_object_dict={
					"name": _name
				}
			)
			print(f"User: {_user.get_json()}")
		elif _user_input == "2":  # get user
			_user_id_string = input("User ID: ")
			_users = None  # type: List[User]
			if _user_id_string == "":
				_users = _user_repository.get(
					database_object_id=None
				)
			else:
				_users = _user_repository.get(
					database_object_id=int(_user_id_string)
				)
			for _user in _users:
				print(f"User: {_user.get_json()}")
		elif _user_input == "3":  # update user
			_user_id = int(input("User ID: "))
			_current_user = _user_repository.get(
				database_object_id=_user_id
			)[0]
			print(f"Current User: {_current_user.get_json()}")
			_name = input("Name: ")
			_current_user.name = _name
			_updated_user = _user_repository.update(
				database_object=_current_user
			)
			print(f"Updated User: {_updated_user.get_json()}")
		elif _user_input == "4":  # remove user
			_user_id_string = input("User ID: ")
			_users = None  # type: List[User]
			if _user_id_string == "":
				_users = _user_repository.remove(
					database_object_id=None
				)
			else:
				_users = _user_repository.remove(
					database_object_id=int(_user_id_string)
				)
			for _user in _users:
				print(f"User: {_user.get_json()}")
		elif _user_input == "5":  # add order
			_product = input("Product: ")
			_user_id = int(input("User ID: "))
			_order = _order_repository.add(
				database_object_dict={
					"product": _product,
					"user_id": _user_id
				}
			)
			print(f"Order: {_order.get_json()}")
		elif _user_input == "6":  # get order
			_order_id_string = input("Order ID: ")
			_orders = None  # type: List[Order]
			if _order_id_string == "":
				_orders = _order_repository.get(
					database_object_id=None
				)
			else:
				_orders = _order_repository.get(
					database_object_id=int(_order_id_string)
				)
			for _order in _orders:
				print(f"Order: {_order.get_json()}")
		elif _user_input == "7":  # update order
			_order_id = int(input("Order ID: "))
			_current_order = _order_repository.get(
				database_object_id=_order_id
			)[0]
			print(f"Current Order: {_current_order.get_json()}")
			_product = input("Product: ")
			_user_id = int(input("User ID: "))
			_current_order.product = _product
			_current_order.user_id = _user_id
			_updated_order = _order_repository.update(
				database_object=_current_order
			)
			print(f"Updated Order: {_updated_order.get_json()}")
		elif _user_input == "8":  # remove order
			_order_id_string = input("Order ID: ")
			_orders = None  # type: List[Order]
			if _order_id_string == "":
				_orders = _order_repository.remove(
					database_object_id=None
				)
			else:
				_orders = _order_repository.remove(
					database_object_id=int(_order_id_string)
				)
			for _order in _orders:
				print(f"Order: {_order.get_json()}")
		elif _user_input == "9":
			_is_active = False
		else:
			print(f"Unexpected user input: \"{_user_input}\".")
	except MemoryDatabaseInterfaceException as ex:
		print(f"MemoryDatabaseInterfaceException: {ex}")
	except RepositoryException as ex:
		print(f"RepositoryException: {ex}")
