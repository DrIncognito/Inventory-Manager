# Inventory Management System

This is a simple inventory management system implemented in Python using SQLite as the database.

## Features

- Add an item to the inventory
- Remove an item from the inventory
- Update item details
- View all items in the inventory
- Audit all items in the inventory

## Classes

### Inventory

This class encapsulates all the operations of the inventory management system.

#### Methods

- `add_item(item_name, quantity, value)`: Adds an item to the inventory.
- `remove_item(item_name)`: Removes an item from the inventory.
- `update_item(item_name, quantity, value)`: Updates the details of an item in the inventory.
- `view_inventory()`: Returns all items in the inventory.
- `audit_inventory()`: Audits all items in the inventory. Asks the user to confirm the quantity and value of each item. If the user does not confirm, it allows the user to edit the item details.
- `help()`: Built in help message on how to use the inventory management library.
## Usage

First, create an instance of the `Inventory` class:

```python
inventory = Inventory()
inventory.add_item("Apple", 100, 0.5)
inventory.remove_item("Apple")
inventory.update_item("Apple", 200, 0.75)
items = inventory.view_inventory()
inventory.audit_inventory()
help_msg = inventory.help()
```