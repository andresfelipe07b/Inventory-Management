class InventoryService:
    # todo crear comentarios documentando todo el código
    def __init__(self):
        self.products = {}

    def add_product(self, name:str, price:float, amount:int)-> None:
        key: str = self._normalize(name)
        if key in self.products.keys():
            print(f"El producto '{name}' ya existe y no se agregó.")
            return
        self.products[key] = (price, amount)
        print(f"\nProducto '{name}' agregado correctamente")

    def get_product(self, name:str)->tuple:
        key:str = self._normalize(name)
        product:tuple = self.products.get(key)
        if product:
            return product
        print(f"No se encontró un producto con el nombre '{name}'.")
        return tuple()


    def remove_product(self, name:str)-> None:
        key:str = self._normalize(name)
        product:tuple = self.products.get(key)
        if product:
            del self.products[key]
            print(f"\nProducto '{name}' eliminado correctamente")
        else:
            print(f"El producto '{name}' no existe.")


    def update_price(self, name:str, new_price:float)-> None:
        key:str = self._normalize(name)
        product:tuple = self.get_product(name)
        if product:
            _, amount = product
            product = (new_price, amount)
            self.products[key] = product
            print(f"Precio de '{name}' actualizado a {new_price:,.2f}")

    def get_total(self)-> float:
        total:float =  sum(price * amount for price, amount in self.products.values())
        print(f"{total:,.2f}")
        return total


    def show_inventory(self)-> None:
        if self.products:
            print("Inventario:")
            for name, (price, amount) in self.products.items():
                print(f"{name}: {price:,.2f} x {amount}")
        else:
            print("El inventario está vacío")




    @staticmethod
    def _normalize(name: str) -> str:
        return name.strip().lower()
