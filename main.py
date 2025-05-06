inventory: list = []

def add_product(products:list,name:str, price:float, amount:int)->list:
    product = {
        "nombre": name,
        "precio": price,
        "cantidad": amount
    }
    products.append(product)
    return products

def get_product(name:str)-> dict:
    print()


