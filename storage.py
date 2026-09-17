import json


def save_products(products):
    with open("data/products.json", "w") as file:
        json.dump(products, file, indent=4)


def load_products():
    with open("data/products.json", "r") as file:
        products = json.load(file)
    return products


def save_customers(customers):
    with open ("data/customers.json", "w") as file:
        json.dump(customers, file, indent=4)


def load_customers():
    with open ("data/customers.json", "r") as file:
        customers = json.load(file)
        return customers

def save_cart(cart):
    with open ("data/cart.json", "w") as file:
        json.dump(cart, file, indent=4)

def load_cart():
    with open("data/cart.json", "r") as file:
        cart = json.load(file)
        return cart