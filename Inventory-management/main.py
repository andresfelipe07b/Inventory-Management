from inventoryService import InventoryService as Inventory # Imports InventoryService class
from utils import request_name, request_amount, request_price # Imports utils to validate inputs values
from utils import RED, YELLOW, RESET # Imports color constants for terminal output


# ------------------- Product Handling Functions -------------------

def handle_add_product(class_inventory: Inventory) -> None:
    """
    Collects product information from the user and adds it to the inventory.

    Args:
        class_inventory (Inventory): The inventory management object
    """
    name: str = request_name("\nEnter the product name: ")
    price: float = request_price("Enter the product price: ")
    amount: int = request_amount("Enter the product quantity: ")
    class_inventory.add_product(name, price, amount)


def handle_get_product(class_inventory: Inventory) -> None:
    """
    Asks for a product name and displays its details if found.

    Args:
        class_inventory (Inventory): The inventory management object
    """
    name: str = request_name("\nEnter the name of the product to search: ")
    product = class_inventory.get_product(name)
    if product != ():
        print(f"Product: \n Name: {name.lower()} \n Price: {product[0]:,.2f}\n Quantity: {product[1]}")


def handle_remove_product(class_inventory: Inventory) -> None:
    """
    Removes a product from the inventory by its name.

    Args:
        class_inventory (Inventory): The inventory management object
    """
    name: str = request_name("\nEnter the name of the product to remove: ")
    class_inventory.remove_product(name)


def handle_update_price(class_inventory: Inventory) -> None:
    """
    Updates the price of an existing product.

    Args:
        class_inventory (Inventory): The inventory management object
    """
    name: str = request_name("\nEnter the product name: ")
    if class_inventory.get_product(name):
        price: float = request_price("Enter the new product price: ")
        class_inventory.update_price(name, price)


def handle_get_total(class_inventory: Inventory)-> None:
    """
    Displays the total value of the inventory.

    Args:
        class_inventory (Inventory): The inventory management object
    """
    total = class_inventory.get_total()
    print(f"Total inventory value: {total:,.2f}")


def handle_show_inventory(class_inventory: Inventory)-> None:
    """
    Displays all products currently stored in the inventory.

    Args:
        class_inventory (Inventory): The inventory management object
    """
    class_inventory.show_inventory()


# ------------------- Menu Interface -------------------

def menu() -> str:
    """
    Displays the main menu and returns the selected option.

    Returns:
        str: User-selected menu option
    """
    print("\n╔════════════════ Options Menu ════════════════╗")
    print("║                                              ║")
    print("║  1. Add product                              ║")
    print("║  2. Search product                           ║")
    print("║  3. Update price                             ║")
    print("║  4. Remove product                           ║")
    print("║  5. Calculate total inventory value          ║")
    print("║  6. Show inventory                           ║")
    print("║  7. Exit                                     ║")
    print("║                                              ║")
    print("╚══════════════════════════════════════════════╝")
    return input("\nChoose an option: ")


# ------------------- Main Program -------------------

def main()-> None:
    """
    Main function that runs the inventory management system.
    """
    inventory = Inventory()
    print("\n--------Inventory Management System---------")

    break_loop: bool = False
    while not break_loop:
        try:
            match menu():
                case "1":
                    handle_add_product(inventory)
                case "2":
                    handle_get_product(inventory)
                case "3":
                    handle_update_price(inventory)
                case "4":
                    handle_remove_product(inventory)
                case "5":
                    handle_get_total(inventory)
                case "6":
                    handle_show_inventory(inventory)
                case "7":
                    print("\nExited successfully!")
                    break_loop = True
                case _:
                    print(f"{YELLOW}Invalid option. Please try again.{RESET}")
        except ValueError:
            print(f"{RED}Error: Please enter a valid option.{RESET}")

# Run the program
main()