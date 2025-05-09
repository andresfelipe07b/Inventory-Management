from inventoryService import InventoryService as Inventory
from utils import request_name, request_amount, request_price
 #todo crear comentarios documentando todo el código



def handle_add_product(class_inventory:Inventory) -> None:
    name: str = request_name("\nIngresa el nombre del producto: ")
    price: float = request_price("Ingresa el precio del producto: ")
    amount: int = request_amount("Ingresa la cantidad del producto: ")
    class_inventory.add_product(name, price, amount)


def handle_get_product(class_inventory:Inventory) -> None:
    name: str = request_name("\nIngresa el nombre del producto que deseas consultar: ")
    product = class_inventory.get_product(name)
    if product != ():
        print(f"Producto: \n Nombre:{name.lower()} \n Precio:{product[0]:,.2f}\n Cantidad:{product[1]}")


def handle_remove_product(class_inventory:Inventory) -> None:
    name: str = request_name("\nIngresa el nombre del producto que deseas eliminar: ")
    class_inventory.remove_product(name)


def handle_update_price(class_inventory:Inventory) -> None:
    name: str = request_name("\nIngresa el nombre del producto: ")
    if class_inventory.get_product(name):
        price: float = request_price("Ingresa el nuevo precio del producto: ")
        class_inventory.update_price(name, price)


def handle_get_total(class_inventory:Inventory):
    total = class_inventory.get_total()
    print(f"Valor total del inventario: {total:,.2f}")

def handle_show_inventory(class_inventory:Inventory):
    class_inventory.show_inventory()

def menu() -> str:
    print("\n1. Agregar producto")
    print("2. Buscar producto")
    print("3. Actualizar precio")
    print("4. Eliminar producto")
    print("5. Calcular valor total del inventario")
    print("6. Mostrar inventario")
    print("7. Salir")
    return input(f"\ningresa una opción: ")


def main():
    inventory = Inventory()
    print("\nSistema de Gestión de Inventario")

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
                    print("\nSalida exitosa!")
                    break_loop = True
                case _:
                    print("La opción que ingresaste no existe. Intentalo nuevamente")
        except ValueError:
            print("Error: ingrese una opción valida")
main()







