import sqlite3

class Inventory:
    """
    This class represents an inventory management system.
    It uses SQLite as the database to store inventory data.
    """

    def __init__(self):
        """
        Constructor method. Establishes a connection to the SQLite database and creates a cursor.
        Also creates the inventory table if it does not exist.
        """
        self.db = sqlite3.connect('inventory_db.sqlite')
        self.cursor = self.db.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS inventory(
                item_name TEXT PRIMARY KEY,  # item_name is the primary key
                quantity INTEGER,  # quantity is the number of items in stock
                value REAL)  # value is the price of the item
        ''')

    def help(self):
        """
        Prints a help message with a description of the class and its methods.
        """
        message = """
        Inventory Management System

        This class represents an inventory management system.
        It uses SQLite as the database to store inventory data.

        Methods:
        - add_item(item_name, quantity, value): Adds an item to the inventory.
        - remove_item(item_name): Removes an item from the inventory.
        - update_item(item_name, quantity, value): Updates the details of an item in the inventory.
        - view_inventory(): Returns all items in the inventory.
        - audit_inventory(): Audits all items in the inventory.

        Usage:
        First, create an instance of the Inventory class:
        inventory = Inventory()

        Then, you can call the methods of the Inventory class to manage the inventory:
        inventory.add_item("Apple", 100, 0.5)
        inventory.remove_item("Apple")
        inventory.update_item("Apple", 200, 0.75)
        items = inventory.view_inventory()
        inventory.audit_inventory()
        """
        print(message)

    def add_item(self, item_name, quantity, value):
        """
        Adds an item to the inventory.
        Raises a ValueError if the item already exists in the inventory.
        """
        try:
            query = "INSERT INTO inventory (item_name, quantity, value) VALUES (?, ?, ?)"
            values = (item_name, quantity, value)
            self.cursor.execute(query, values)
            self.db.commit()
        except sqlite3.IntegrityError:
            raise ValueError("Item already exists in the inventory. Use the update option instead.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def remove_item(self, item_name):
        """
        Removes an item from the inventory.
        """
        try:
            query = "DELETE FROM inventory WHERE item_name = ?"
            values = (item_name,)
            self.cursor.execute(query, values)
            self.db.commit()
        except Exception as e:
            print(f"An error occurred: {e}")

    def update_item(self, item_name, quantity, value):
        """
        Updates the details of an item in the inventory.
        """
        try:
            query = "UPDATE inventory SET quantity = ?, value = ? WHERE item_name = ?"
            values = (quantity, value, item_name)
            self.cursor.execute(query, values)
            self.db.commit()
        except Exception as e:
            print(f"An error occurred: {e}")

    def view_inventory(self):
        """
        Returns all items in the inventory.
        """
        self.cursor.execute("SELECT * FROM inventory")
        rows = self.cursor.fetchall()
        return rows

    def audit_inventory(self):
        """
        Audits all items in the inventory.
        Asks the user to confirm the quantity and value of each item.
        If the user does not confirm, it allows the user to edit the item details.
        """
        items = self.view_inventory()
        for item in items:
            item_name, quantity, value = item
            print(f"\nItem: {item_name}\nQuantity: {quantity}\nValue: {value}")
            confirm = input("Are the quantity and value correct? (yes/no): ")
            if confirm.lower() != "yes":
                new_quantity = int(input("Enter the new quantity: "))
                new_value = float(input("Enter the new value: "))
                self.update_item(item_name, new_quantity, new_value)
            else:
                print("The quantity and value are confirmed.")