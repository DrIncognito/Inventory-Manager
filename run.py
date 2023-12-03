from rich.console import Console
from rich.table import Table
from inventory import Inventory
import os

def display_inventory(console, inventory):
    # Create a table
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Item Name")
    table.add_column("Quantity")
    table.add_column("Value")
    table.add_column("Total Value")

    # Load data and add to the table
    data = inventory.view_inventory()
    for row in data:
        total_value = row[1] * row[2]
        table.add_row(str(row[0]), str(row[1]), str(row[2]), str(total_value))

    # Print the table to the console
    console.print(table)


def main():
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')


    # Create a console object
    console = Console()

    # Create an inventory object
    inventory = Inventory()
    
    # Display the inventory by default
    display_inventory(console, inventory)

    while True:
        console.print("\n[1] Add item")
        console.print("[2] Remove item")
        console.print("[3] Update item")
        console.print("[4] View inventory")
        console.print("[5] Audit inventory")
        console.print("[6] Help")
        console.print("[7] Exit")

        choice = input("\nEnter your choice: ")

        try:
            if choice == '1':
                item_name = input("Enter item name: ")

                # Check if the item already exists
                if inventory.item_exists(item_name):
                    clear_screen()
                    console.print("Item already exists in the inventory. Use the update option instead.")
                    input("Press enter to continue...")
                    continue

                quantity = int(input("Enter quantity: "))
                value = float(input("Enter value: "))

                inventory.add_item(item_name, quantity, value)
                console.print(f"Added {quantity} of {item_name} with value {value}")
            elif choice == '2':
                item_name = input("Enter item name: ")

                inventory.remove_item(item_name)
                console.print(f"Removed {item_name} from inventory")
            elif choice == '3':
                item_name = input("Enter item name: ")

                if not inventory.item_exists(item_name):
                    console.print("Item does not exist in the inventory. Use the add option instead.")
                    input("Press any key to continue...")
                    continue

                console.print("What would you like to update?")
                console.print("[1] Quantity")
                console.print("[2] Value")
                console.print("[3] Both")

                update_choice = input("Enter your choice: ")

                if update_choice == '1':
                    quantity = int(input("Enter the new quantity: "))
                    inventory.update_item(item_name, quantity=quantity)
                elif update_choice == '2':
                    value = float(input("Enter the new value: "))
                    inventory.update_item(item_name, value=value)
                elif update_choice == '3':
                    quantity = int(input("Enter the new quantity: "))
                    value = float(input("Enter the new value: "))
                    inventory.update_item(item_name, quantity=quantity, value=value)
                else:
                    console.print("Invalid choice. Please try again.")
            elif choice == '4':
                display_inventory(console, inventory)
            elif choice == '5':
                inventory.audit_inventory()
            elif choice == '6':
                inventory.help()
            elif choice == '7':
                break
            else:
                console.print("Invalid choice. Please try again.")
        except ValueError as e:
            clear_screen()
            console.print(e)
            input("Press enter to continue...")
        except Exception as e:
            clear_screen()
            console.print(f"An error occurred: {e}")
            input("Press enter to continue...")

        # Display the inventory after each choice
        display_inventory(console, inventory)

if __name__ == "__main__":
    main()