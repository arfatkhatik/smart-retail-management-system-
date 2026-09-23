

import storage
def search():
    print("""
    ========================================
                  SEARCH
    ========================================

        1. Search Products
        2. Search Customers
        3. back

    ========================================
    """)

    user_option = input("Enter your option: ")
    if user_option in ("1", "search products"):
        search_products()
    elif user_option in ("2", "search customers"):
        search_customers()
    elif user_option in ("3", "back"):
        return
    else:
        print("invalid option")

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


def search_customers():
    customers = storage.load_customers()
    if not customers:
        print("No customer found.")
        return
    print("=" * 40)
    print("         SEARCH CUSTOMERS")
    print("=" * 40)
            
    print("1. customer id")
    print("2. name")
    print("3. phone")
    print("4. email")
    print("5. address")
    print("=" * 40)


    option = input("Enter your option: ")

    search_field = {
        "1": "customer_id",
        "2": "name",
        "3": "phone",
        "4": "email",
        "5": "address"
    }
    search_field = search_field.get(option)

    if search_field is None:
        print("invalid option.")
        return

    search_value = input(f"Enter {search_field} to search: ").lower().strip()

    found = False

    for customer in customers:
        if search_value in str(customer[search_field]).lower():
            found = True
            print("=" * 50)
            print(f"customer ID: {customer['customer_id']}")
            print(f"customer name: {customer['name']}")
            print(f"customer Phone: {customer['phone']}")
            print(f"customer Email: {customer['email']}")
            print(f"customer address: {customer['address']}")
            print("=" * 50)

    if not found:
        print("No matching customer found.")
        return
