from inventoryService import InventoryService as Inventory, InventoryService
from utils import request_name, request_amount, request_price
 #todo crear comentarios documentando todo el código


def main():
    inventory = Inventory()

    def handle_add_product()-> None:

        name:str = request_name("Ingresa el nombre del producto: ")
        price:float = request_price("Ingresa el precio del producto: ")
        amount:int = request_amount("Ingresa la cantidad del producto: ")
        inventory.add_product(name, price, amount)

    def handle_get_product()-> None:

        name:str = request_name("Ingresa el nombre del producto que deseas consultar: ")
        product = inventory.get_product(name)
        if product != ():
           print(f"Producto: \n Nombre:{name} \n Precio:{product[0]:,.2f}\n Cantidad:{product[1]}")


    def handle_remove_product()-> None:
        name:str = request_name("Ingresa el nombre del producto que deseas eliminar: ")
        inventory.remove_product(name)
        print(f"Producto '{name}' eliminado correctamente")

    #todo probar, agregar funcionalidad para crear un nuevo producto a partir de una entrada
    def handle_update_price()-> None:
        name:str = request_name("Ingresa el nombre del producto: ")
        price:float = request_price("Ingresa el nuevo precio del producto: ")
        inventory.update_price(name, price)

    def handle_get_total():
        total = inventory.get_total()
        print(f"Valor total del inventario: {total:,.2f}")


    def menu()-> str:

        print("\n1. Agregar producto")
        print("2. Buscar producto")
        print("3. Actualizar precio")
        print("4. Eliminar producto")
        print("5. Calcular valor total del inventario")
        print("6. Mostrar inventario")
        print("7. Salir")
        return input(f"\ningresa una opción: ")



    print("\nSistema de Gestión de Inventario")

    break_loop: bool = False
    while not break_loop:
        try:
            match menu():
                case "1":
                    handle_add_product()
                case "2":
                    handle_get_product()
                case "3":
                    handle_update_price()
                case "4":
                    handle_remove_product()
                case "5":
                    handle_get_total()
                #todo crear case: mostrar todo el inventario
                #case "6":
                case "6":
                    print("\nSalida exitosa!")
                    break_loop = True
                case _:
                    print("La opción que ingresaste no existe. Intentalo nuevamente")
        except ValueError:
            print("Error: ingrese una opción valida")



main()







