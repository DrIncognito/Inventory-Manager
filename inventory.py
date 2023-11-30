import sqlite3
import pandas as pd

# Establish a connection to the SQLite database
# If the database does not exist, it will be created
db = sqlite3.connect('inventory_db.sqlite')

cursor = db.cursor()

# Create the inventory table if it does not exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS inventory(
        item_name TEXT PRIMARY KEY,
        quantity INTEGER,
        price REAL)
''')

# Function to add an item to the inventory
def add_item(item_name, quantity, price):
    query = "INSERT INTO inventory (item_name, quantity, price) VALUES (?, ?, ?)"
    values = (item_name, quantity, price)
    cursor.execute(query, values)
    db.commit()

# Function to remove an item from the inventory
def remove_item(item_name):
    query = "DELETE FROM inventory WHERE item_name = ?"
    values = (item_name,)
    cursor.execute(query, values)
    db.commit()

# Function to update item details
def update_item(item_name, quantity, price):
    query = "UPDATE inventory SET quantity = ?, price = ? WHERE item_name = ?"
    values = (quantity, price, item_name)
    cursor.execute(query, values)
    db.commit()

# Function to view the inventory
def view_inventory():
    cursor.execute("SELECT * FROM inventory")
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=['Item Name', 'Quantity', 'Price'])
    print(df)

    