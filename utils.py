# todo crear comentarios documentando todo el código
def request_name(msg:str)->str:

    while True:
       try:
           name:str = input(msg).strip()
           if name.replace(" ", "").isalpha():
               return name
           print(f"El nombre no debe estar vacío ni ser numérico.")
       except ValueError:
           print(f"Error: ingrese un nombre válido")


def request_price(msg:str)->float:
    while True:
       try:
           price:float = float(input(msg))
           if price <= 1:
                print(f"El precio debe ser mayor que 0.")
           else:
                return price
       except ValueError:
           print(f"Error: ingrese un valor numérico.")

def request_amount(msg:str)->int:
    while True:
       try:
           amount:int = int(input(msg))
           if not( 0 < amount <= 100000000) :
                print(f"la cantidad debe ser mayor que 0 y menor que 100.000.000.")
           else:
                return amount
       except ValueError:
           print(f"Error: ingrese un valor numérico")
