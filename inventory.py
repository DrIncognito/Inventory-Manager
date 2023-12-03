import sqlite3

class Inventory:
    def __init__(self):
        self.db = sqlite3.connect('inventory_db.sqlite')
        self.cursor = self.db.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS inventory(
                item_name TEXT PRIMARY KEY,
                quantity INTEGER,
                value REAL)
        ''')

    def add_item(self, item_name, quantity, value):
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
        try:
            query = "DELETE FROM inventory WHERE item_name = ?"
            values = (item_name,)
            self.cursor.execute(query, values)
            self.db.commit()
        except Exception as e:
            print(f"An error occurred: {e}")

    def update_item(self, item_name, quantity, value):
        try:
            query = "UPDATE inventory SET quantity = ?, value = ? WHERE item_name = ?"
            values = (quantity, value, item_name)
            self.cursor.execute(query, values)
            self.db.commit()
        except Exception as e:
            print(f"An error occurred: {e}")

    def view_inventory(self):
        self.cursor.execute("SELECT * FROM inventory")
        rows = self.cursor.fetchall()
        return rows

    def audit_inventory(self):
        items = self.view_inventory()
        for item in items:
            item_name, quantity, value = item
            print(f"\nItem: {item_name}\nQuantity: {quantity}\nValue: {value}")
            confirm = input("Are the quantity and value correct? (yes/no): ")
            if confirm.lower() != "yes":
                new_quantity = int(input("Enter the new quantity: "))
                new_value = float(input("Enter the new value: "))
                self.update_item(item_name, new_quantity, new_value)