from utils import YELLOW, RESET, GREEN


class InventoryService:
    """
    Manages a simple inventory of products with their prices and quantities.
    """

    def __init__(self):
        # Stores products using their names as keys and (price, amount) as values
        self.products = {}

    def add_product(self, name: str, price: float, amount: int) -> None:
        """
        Adds a new product to the inventory if it doesn't already exist.

        Args:
            name (str): Product name
            price (float): Product price
            amount (int): Product quantity
        """
        key: str = self._normalize(name)
        if key in self.products.keys():
            print(f"{YELLOW}The product '{name}' already exists and was not added.{RESET}")
            return
        self.products[key] = (price, amount)
        print(f"\n{GREEN}Product '{name}' added successfully.{RESET}")

    def get_product(self, name: str) -> tuple:
        """
        Retrieves a product by name from the inventory.

        Args:
            name (str): Product name to look for

        Returns:
            tuple: (price, amount) if found, otherwise empty tuple
        """
        key: str = self._normalize(name)
        product: tuple = self.products.get(key)
        if product:
            return product
        print(f"{YELLOW}No product found with the name '{name}'.{RESET}")
        return tuple()

    def remove_product(self, name: str) -> None:
        """
        Removes a product from the inventory by name.

        Args:
            name (str): Product name to remove
        """
        key: str = self._normalize(name)
        product: tuple = self.products.get(key)
        if product:
            del self.products[key]
            print(f"{GREEN}\nProduct '{name}' removed successfully.{RESET}")
        else:
            print(f"{YELLOW}The product '{name}' does not exist.{RESET}")

    def update_price(self, name: str, new_price: float) -> None:
        """
        Updates the price of an existing product.

        Args:
            name (str): Product name
            new_price (float): New price to assign
        """
        key: str = self._normalize(name)
        product: tuple = self.get_product(name)
        if product:
            _, amount = product
            product = (new_price, amount)
            self.products[key] = product
            print(f"{GREEN}Price of '{name}' updated to {new_price:,.2f}{RESET}")

    def get_total(self) -> float:
        """
        Calculates the total inventory value.

        Returns:
            float: Total value of all products
        """
        total: float = sum(price * amount for price, amount in self.products.values())
        return total

    def show_inventory(self) -> None:
        """
        Displays the list of products in the inventory.
        """
        if self.products:
            print("Inventory:")
            for name, (price, amount) in self.products.items():
                print(f"{name}: {price:,.2f} x {amount}")
        else:
            print(f"{YELLOW}The inventory is empty{RESET}.")

    @staticmethod
    def _normalize(name: str) -> str:
        """
        Normalizes a product name for consistent key handling.

        Args:
            name (str): The original product name

        Returns:
            str: Normalized version of the name
        """
        return name.strip().lower()