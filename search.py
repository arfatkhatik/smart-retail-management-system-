

import storage
def search():
    print("""
    ========================================
                  SEARCH
    ========================================

        1. Search Products
        2. Search Customers
        3. Search Orders
        4. Back

    ========================================
    """)

    user_option = input("Enter your option: ")
    if user_option in ("1", "search products"):
        search_products()

def search_products():
    products = storage.load_products()
    if not products:
        print("No product found.")
        return
    print("=" * 40)
    print("         SEARCH PRODUCTS")
    print("=" * 40)

    print("1. Product ID")
    print("2. Name")
    print("3. Category")
    print("4. Brand")
    print("5. Supplier")

    option = input("Enter your option: ").lower().strip()

    search_field = {
        "1": "product id",
        "2": "name",
        "3": "category",
        "4": "brand name",
        "5": "supplier name"
    }
    search_field = search_field.get(option)

    if search_field is None:
        print("Invalid option.")
        return

    search_value = input(f"Enter {search_field} to search: ").lower().strip()

    found = False

    for product in products:
        if search_value in str(product[search_field]).lower():
            found = True
            print("=" * 50)
            print(f"Product ID: {product['product id']}")
            print(f"Name: {product['name']}")
            print(f"Category: {product['category']}")
            print(f"Brand: {product['brand name']}")
            print(f"Supplier: {product['supplier name']}")
            print(f"Selling Price: ₹{product['selling price']}")
            print(f"Stock: {product['stock quantity']}")
            print("=" * 50)

        if not found:
            print("No matching product found.")
            return