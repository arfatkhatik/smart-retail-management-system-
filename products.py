from itertools import product
import json
import os
import storage
def product_manager():
    while True:
        print("""
        ======================================================================================

                                     PRODUCT MANAGEMENT

        ======================================================================================

        -----------------------------
            1. add product
            2. view products
            3. search product
            4. update product
            5. delete product
            6. back to main menu
        -----------------------------

        ======================================================================================
        """)
        user_input: str = input("enter your option: ")
        if user_input in ("1", "add product"):
            add_product()
        elif user_input in ("2", "view product", "view products"):
            view_product()
        elif user_input in ("3", "search"):
            search_product()
        elif user_input in ("4", "update product"):
            update_product()
        elif user_input in ("5", "delete product"):
            delete_product()
        elif user_input in ("6", "back to main menu"):
            break
        else:
            print("Invalid option.")


def add_product():
    products = storage.load_products()
    product_id = input("enter product id: ")
    name = input("enter product name: ")
    category = input("enter product category: ")
    brand = input("enter product brand: ")
    purchase_price = int(input("enter the purchase price of product: "))
    selling_price = int(input("enter the selling price of product: "))
    stock_quantity = int(input("Enter stock quantity: "))
    minimum_stock = int(input("Enter minimum stock level: "))
    supplier = input("Enter supplier: ")
    description = input("Enter product description: ")

    product = {
        "product id": product_id,
        "name": name,
        "category": category,
        "brand name": brand,
        "purchase price": purchase_price,
        "selling price": selling_price,
        "stock quantity": stock_quantity,
        "minimum stock": minimum_stock,
        "supplier name": supplier,
        "description": description,
    }

    products.append(product)
    storage.save_products(products)
    print(f"Product '{name}' added successfully.")


def view_product():
    products = storage.load_products()
    count = 1
    if not products:
        print("No products found.")
        return

    print("=" * 60)
    print("                     PRODUCTS LIST")
    print("=" * 60)

    for product in products:
        print(f"            product#{count}")
        _print_product(product)
        count += 1


def search_product():
    print("=" * 60)
    print("             SEARCH PRODUCTS")
    print("=" * 60)
    print("1. search by id")
    print("2. search by name")
    print("3. search by category")
    print("4. search by brand")
    print("5. search by supplier")
    print("6. back")
    print("=" * 60)
    user_input = input("enter your option: ")
    if user_input in ("1", "search by id"):
        searchby_id()
    elif user_input in ("2", "search by name"):
        searchby_name()
    elif user_input in ("3", "search by category"):
        searchby_category()
    elif user_input in ("4", "search by brand"):
        searchby_brand()
    elif user_input in ("5", "search by supplier"):
        searchby_supplier()
    elif user_input in ("6", "back"):
        return
    

def _print_product(product):
    print("-" * 60)
    print(f"Product ID:       {product['product id']}")
    print(f"Product name:     {product['name']}")
    print(f"Category:         {product['category']}")
    print(f"Brand name:       {product['brand name']}")
    print(f"Purchase price:   {product['purchase price']}")
    print(f"Selling price:    {product['selling price']}")
    print(f"Stock quantity:   {product['stock quantity']}")
    print(f"Minimum stock:    {product['minimum stock']}")
    print(f"Supplier name:    {product['supplier name']}")
    print(f"Description:      {product['description']}")
    print("-" * 60)


def searchby_id():
    products = storage.load_products()
    search_term = input("enter id to search product: ").strip().lower()
    found = False

    for product in products:
        product_id = str(product["product id"]).lower()
        if product_id == search_term:
            _print_product(product)
            found = True

    if not found:
        print("No product found with that ID.")

def searchby_name():
    products = storage.load_products()
    search_term = input("enter name to search product: ").strip().lower()
    found = False

    for product in products:
        name = str(product["name"]).lower()
        if name == search_term:
            _print_product(product)
            found = True
    if not found:
        print("No product with that name ")

def searchby_category():
    products = storage.load_products()
    search_term = input("enter category to search product: ").strip().lower()
    found = False 

    for product in products:
        category = str(product["category"]).lower()
        if category == search_term:
            _print_product(product)
            found = True
    if not found:
        print("No product found in that category")

def searchby_brand():
    products = storage.load_products()
    search_term = input("enter brand name to search prodcut: ").strip().lower()
    found = False

    for product in products:
        brand = str(product["brand"]).lower()
        if brand == search_term:
            _print_product(product)
            found = True
    if not found:
        print("No Product found of that brand")

def searchby_supplier():
    products = storage.load_products
    search_term = input("enter supplier name to search product: ").strip().lower()
    found = False

    for product in products:
        supplier = str(product["supplier"]).lower()
        if supplier == search_term:
            _print_product(product)
            found = True
        if not found:
            print("No product found of that supplier")

def update_product():
    products = storage.load_products()
    search_term = input("enter id of product to update: ").strip().lower()
    found = False

    for product in products:
        product_id = str(product["product id"]).lower()
        if product_id == search_term:
            print("What would you like to update?")
            print("=" * 60)
            print("            what should you like to update?")
            print("=" * 60)
            print("1. name")
            print("2. category")
            print("3. brand")
            print("4. purchase price")
            print("5. selling price")
            print("6. stock quantity")
            print("7. minimum stock")
            print("8. supplier")
            print("9. description")
            print("10. cancel")
            found = True
            while True:
                try:
                    choice = int(input("enter your choice: "))
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
                else:
                    if choice < 1 or choice > 10:
                        print("Invalid choice. Please select a valid option.")
                        continue
                    
                break
            if choice == 1:
                product["name"] = input("enter new name: ")
            elif choice == 2:
                product["category"] = input("enter new category: ")
            elif choice == 3:
                product["brand name"] = input("enter new brand: ")
            elif choice == 4:
                try:
                    product["purchase price"] = int(input("enter new purchase price: "))
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            elif choice == 5:
                try:
                    product["selling price"] = int(input("enter new selling price: "))
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            elif choice == 6:
                product["stock quantity"] = int(input("enter new stock quantity: "))
            elif choice == 7:
                product["minimum stock"] = int(input("enter new minimum stock quantity: "))
            elif choice == 8:
                product["supplier name"] = input("enter new supplier name: ")
            elif choice == 9:
                product["description"] = input("enter new description: ")
            elif choice == 10:
                print("Update cancelled.")
                return
            storage.save_products(products)
        if not found:
            print("No product found with that ID.")

def delete_product():
    products = storage.load_products()
    search_term = input("enter id of product to delete: ").strip().lower() 
    for product in products:
        product_id = str(product['product id']).lower()
        if product_id == search_term:
            print(product)
            confirmation =input(f"do you really wanted to delete :{product['name']} yes or no: " ).lower().strip()
            if confirmation == "yes":
                products.remove(product)
                storage.save_products(products)
                print(f"product {product['name']} deleted successfully.")
                return
            elif confirmation == "no":
                print("canceled delitation")
                return
        