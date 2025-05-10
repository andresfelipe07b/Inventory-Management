# ------------------- Input Validation Utilities -------------------

# Color constants for terminal output
RED:str = '\033[91m'
GREEN:str = '\033[92m'
YELLOW:str = '\033[93m'
RESET:str = '\033[0m'

def request_name(msg: str) -> str:
    """
    Prompts the user to enter a valid product name.

    Args:
        msg (str): The message to display when asking for input

    Returns:
        str: A validated product name (alphabetic, non-empty)
    """
    while True:
        try:
            name: str = input(msg).strip()
            if name.replace(" ", "").isalpha():
                return name
            print(f"{YELLOW}The name must not be empty or numeric.{RESET}")
        except ValueError:
            print(f"{RED}Error: Please enter a valid name.{RESET}")


def request_price(msg: str) -> float:
    """
    Prompts the user to enter a valid price.

    Args:
        msg (str): The message to display when asking for input

    Returns:
        float: A positive float representing the product price
    """
    while True:
        try:
            price: float = float(input(msg))
            if price <= 1:
                print(f"{YELLOW}The price must be greater than 0.{RESET}")
            else:
                return price
        except ValueError:
            print(f"{RED}Error: Please enter a numeric value.{RESET}")


def request_amount(msg: str) -> int:
    """
    Prompts the user to enter a valid quantity for a product.

    Args:
        msg (str): The message to display when asking for input

    Returns:
        int: Quantity value between 1 and 100,000,000
    """
    while True:
        try:
            amount: int = int(input(msg))
            if not (0 < amount <= 100000000):
                print(f"{YELLOW}Quantity must be greater than 0 and less than 100,000,000.{RESET}")
            else:
                return amount
        except ValueError:
            print(f"{RED}Error: Please enter a numeric value.{RESET}")
