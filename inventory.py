import sqlite3
import pandas as pd

# Establish a connection to the SQLite database
# If the database does not exist, it will be created
# This is done using the connect() function from the sqlite3 module
db = sqlite3.connect('inventory_db.sqlite')

# Create a cursor object
# The cursor is used to traverse the records from the result set
cursor = db.cursor()

# Create the inventory table if it does not exist
# The execute() function is used to perform SQL commands
# The table has three columns: item_name, quantity, and value
cursor.execute('''
    CREATE TABLE IF NOT EXISTS inventory(
        item_name TEXT PRIMARY KEY,  # item_name is the primary key
        quantity INTEGER,  # quantity is the number of items in stock
        value REAL)  # value is the price of the item
''')

# Function to add an item to the inventory
def add_item(item_name, quantity, value):
    """
    This function adds an item to the inventory.
    It takes three parameters: item_name, quantity, and value.
    It raises a ValueError if the item already exists in the inventory.
    """
    try:
        # Prepare the query and values
        query = "INSERT INTO inventory (item_name, quantity, value) VALUES (?, ?, ?)"
        values = (item_name, quantity, value)
        
        # Execute the query
        cursor.execute(query, values)
        
        # Commit the transaction
        db.commit()
    except sqlite3.IntegrityError:
        raise ValueError("Item already exists in the inventory. Use the update option instead.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to remove an item from the inventory
def remove_item(item_name):
    """
    This function removes an item from the inventory.
    It takes one parameter: item_name.
    """
    try:
        # Prepare the query and values
        query = "DELETE FROM inventory WHERE item_name = ?"
        values = (item_name,)
        
        # Execute the query
        cursor.execute(query, values)
        
        # Commit the transaction
        db.commit()
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to update item details
def update_item(item_name, quantity, value):
    """
    This function updates the details of an item in the inventory.
    It takes three parameters: item_name, quantity, and value.
    """
    try:
        # Prepare the query and values
        query = "UPDATE inventory SET quantity = ?, value = ? WHERE item_name = ?"
        values = (quantity, value, item_name)
        
        # Execute the query
        cursor.execute(query, values)
        
        # Commit the transaction
        db.commit()
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to view the inventory
def view_inventory():
    """
    This function returns all items in the inventory.
    """
    # Execute the query
    cursor.execute("SELECT * FROM inventory")
    
    # Fetch all the rows
    rows = cursor.fetchall()
    
    return rows