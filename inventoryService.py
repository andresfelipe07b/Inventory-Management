class InventoryService:

    def __init__(self):
        self.products = {}

    def add_product(self, name:str, price:float, amount:int):
        for product in self.products.keys():
            if product == name:
                print(f"El {product} no se agregó debido a que ya existe")
                return
        self.products[name] = (price, amount)
        print(f"Producto agregado correctamente")

    def get_product(self, name:str)->tuple:
        for product in self.products.keys():
            if product == name:
                return self.products[product]
        print(f"El producto {name} no existe")
        return tuple()

    def remove_product(self, name:str):
        for product in self.products.keys():
            if product == name:
                del self.products[product]
                print(f"El producto {name} se ha eliminado correctamente")
                return

    def update_product(self, name:str, price:float, amount:int):
        for product in self.products.keys():
            if product == name:
                self.products[product] = (price, amount)
                print(f"El producto {name} se ha actualizado correctamente")



