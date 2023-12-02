from rich.console import Console
from rich.table import Table
from inventory import add_item, remove_item, update_item, view_inventory

def display_inventory(console):
    # Create a table
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Item Name")
    table.add_column("Quantity")
    table.add_column("Value")
    table.add_column("Total Value")

    # Load data and add to the table
    data = view_inventory()
    for row in data:
        total_value = row[1] * row[2]
        table.add_row(str(row[0]), str(row[1]), str(row[2]), str(total_value))

    # Print the table to the console
    console.print(table)

def main():
    # Create a console object
    console = Console()

    # Display the inventory by default
    display_inventory(console)

    while True:
        console.print("\n[1] Add item")
        console.print("[2] Remove item")
        console.print("[3] Update item")
        console.print("[4] View inventory")
        console.print("[5] Exit")

        choice = input("\nEnter your choice: ")

        try:
            if choice == '1':
                item_name = input("Enter item name: ")
                quantity = int(input("Enter quantity: "))
                value = float(input("Enter value: "))

                add_item(item_name, quantity, value)
                console.print(f"Added {quantity} of {item_name} with value {value}")
            elif choice == '2':
                item_name = input("Enter item name: ")

                remove_item(item_name)
                console.print(f"Removed {item_name} from inventory")
            elif choice == '3':
                item_name = input("Enter item name: ")
                quantity = int(input("Enter quantity: "))
                value = float(input("Enter value: "))

                update_item(item_name, quantity, value)
                console.print(f"Updated {item_name} to {quantity} with value {value}")
            elif choice == '4':
                display_inventory(console)
            elif choice == '5':
                break
            else:
                console.print("Invalid choice. Please try again.")
        except ValueError as e:
            console.print(e)
        except Exception as e:
            console.print(f"An error occurred: {e}")

        except ValueError:
            console.print("Invalid input. Please enter the correct type of value.")
        except Exception as e:
            console.print(f"An error occurred: {e}")

        # Display the inventory after each choice
        display_inventory(console)

if __name__ == "__main__":
    main()