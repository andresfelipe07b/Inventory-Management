# todo crear comentarios documentando todo el código
def request_name(msg:str)->str:

    while True:
       try:
           name:str = input(msg).strip()
           if not name.isnumeric() or len(name) < 1:
               return name
           print(f"El nombre no debe estar vacío ni ser numérico.")
       except ValueError:
           print(f"Error: ingrese un nombre válido")


def request_price(msg:str)->float:
    while True:
       try:
           price:float = float(input(msg))
           if price <= 0:
                print(f"El precio debe ser mayor que 0.")
           else:
                return price
       except ValueError:
           print(f"Error: ingrese un valor numérico.")

def request_amount(msg:str)->int:
    while True:
       try:
           amount:int = int(input(msg))
           if amount <= 0:
                print(f"la cantidad debe ser mayor que 0.")
           else:
                return amount
       except ValueError:
           print(f"Error: ingrese un valor numérico")
