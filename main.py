inventory: list = [{"nombre": "andres", "precio": 2000}]

def add_product(products:list,name:str, price:float, amount:int)->list:
    product = {
        "nombre": name,
        "precio": price,
        "cantidad": amount
    }
    products.append(product)
    return products

def get_product(name:str, products: list)-> dict:
    product = list(filter(lambda x: x["nombre"] == name, products))
    return product[0] if product else {}



# print(inventory)
print(get_product("andres", inventory))


