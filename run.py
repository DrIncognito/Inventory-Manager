from rich.console import Console
from rich.table import Table
from inventory import add_item
from inventory import remove_item
from inventory import update_item


def load_data():
    # Implement your logic to load data here
    # For example, you can return a list of tuples representing the data
    return [("Item 1", 10, 5.99), ("Item 2", 5, 9.99), ("Item 3", 2, 14.99)]


def main():
    # Create a console object
    console = Console()

    while True:
        console.print("[1] Add item")
        console.print("[2] Remove item")
        console.print("[3] Update item")
        console.print("[4] View inventory")
        console.print("[5] Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))

            add_item(item_name, quantity, price)
        elif choice == '2':
            item_name = input("Enter item name: ")

            remove_item(item_name)
        elif choice == '3':
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))

            update_item(item_name, quantity, price)
        elif choice == '4':
            # Create a table
            table = Table(show_header=True, header_style="bold magenta")

            table.add_column("Item Name")
            table.add_column("Quantity")
            table.add_column("Price")

            # Load data and add to the table
            data = load_data()
            for row in data:
                table.add_row(str(row[0]), str(row[1]), str(row[2]))

            # Print the table to the console
            console.print(table)
        elif choice == '5':
            break
        else:
            console.print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()