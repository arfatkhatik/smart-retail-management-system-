import json


def save_products(products):
    with open("data/products.json", "w") as file:
        json.dump(products, file, indent=4)


def load_products():
    with open("data/products.json", "r") as file:
        products = json.load(file)
    return products