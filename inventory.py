import storage
def inventry_manager():
    print("""
        ========================================
                   INVENTORY MANAGEMENT
        ========================================

            1. View Inventory
            2. Restock Product
            3. Check Low Stock
            4. Check Out-of-Stock Products
            5. Adjust Stock
            6. Back to Main Menu

        ========================================

""")
    user_option = input("Enter your option: ").lower().strip()
    if user_option in ("1", "view inventory"):
        view_inventory()
    elif user_option in ("2", "restock product"):
        restock_product()
    elif user_option in ("3", "check low stock"):
        check_low_stock()

def view_inventory():
    products = storage.load_products()
    print("=" * 30)
    print("       INVENTORY")
    print("=" * 30)

    for product in products:
        print(f"Product ID: {product['product id']}")
        print(f"Name: {product['name']}")
        print(f"Category: {product['category']}")
        print(f"Stock: {product['stock quantity']}")
        print(f"Minimum Stock: {product['minimum stock']}")
        print("-" * 30)


def restock_product():
    products =storage.load_products()
    product_id = input("Enter product ID: ")

    found = False
    for product in products:
        if product['product id'] == product_id:
            found = True
            print(f"product ID: {product['product id']}")
            print(f"product name: {product['name']}")
            print(f"current stock: {product['stock quantity']}")
            restock = int(input("Enter quantity to add: "))
            product['stock quantity'] += restock

            storage.save_products(products)
            print("Product restocked successfully.")

            break


    if not found:
        print("product not found")
        return


def check_low_stock():
    products = storage.load_products()
    found = False
    for product in products:
        if product['stock quantity'] <= product['minimum stock']:
            found = True
            print("=" * 50)
            print(f"product ID: {product['product id']}")
            print(f"product name: {product['name']}")
            print(f"current stock: {product['stock quantity']}")
            print(f"minimum quantity: {product['minimum stock']}")
            print("-" * 50)
    if not found:
        print("No low-stock products.")
        return

