def cart_manager():
    
    print("""
    ===============================[ SHOPPING CART MENU ]===============================

    --------------------------------
    1. add product to cart
    2. remove product from cart
    3. view cart
    4. total price
    5. back
    --------------------------------
    
    ===============================[ CHOOSE YOUR OPTION ]===============================

    """)
    user_option = input("Enter your option: ")
    if user_option in ("1", "add product to cart"):
        add_product_to_cart()
    elif user_option in ("2", "remove product from cart"):
        remove_cart()
    elif user_option in ("3", "view cart"):
        view_cart()
    elif user_option in ("4", "total price"):
        total_cart()
    elif user_option in ("5", "back"):
        return
    else:
        print("Invalid option selected")



import storage
def add_product_to_cart():
    customer = get_or_create_customers()
    products = storage.load_products()
    customer_id = customer["customer_id"]
    cart = storage.load_cart()

    customer_cart = None

    for saved_cart in cart:
        if saved_cart.get("customer_id") == customer_id:
            customer_cart = saved_cart
            break

    if customer_cart is None:
        customer_cart = {
            "customer_id": customer_id,
            "items": []
        }
        cart.append(customer_cart)
        storage.save_cart(cart)

    categories = set()
    for product in products:
        categories.add(product['category'])

    print("============================[ CATEGORIES ]===============================")
    print("these are the categories which we have in our store...")
    count = 1
    for category in categories:
        print(f"{count}. {category}")
        count += 1
    print("NOTE: please enter the category name in which you want to shop...")
    print("============================================================================")

    category = input("Enter the category: ").strip()
    
    if category in categories:
        print("these are the products which we have in this category...")
        for product in products:
            if product['category'] == category or product['category'] == category.lower().strip() or product['category'] == category.upper().strip():
                print("============================================================================")

                print(f"1. product id: {product['product id']}")
                print(f"2. product name: {product['name']}")
                print(f"3. product brand: {product['brand name']}")
                print(f"4. product price: ₹{product['selling price']}")
                print(f"5. product quantity: {product['stock quantity']}")

                print("============================================================================")

    product_id = input("Enter product ID to add to cart: ").strip()
    found = False

    for product in products:
        if product['product id'] == product_id:
            found = True
            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                return

            if quantity > product['stock quantity']:
                print("Not enough stock available")
                return

            cart_item = {
                "product_id": product["product id"],
                "product name": product["name"],
                "price": product["selling price"],
                "quantity": quantity
            }
            customer_cart["items"].append(cart_item)
            storage.save_cart(cart)
            print("product added to cart successfully")
            return

    if not found:
        print("No product with that ID. Please enter a valid ID.")
        return

def remove_cart():
    cart = storage.load_cart()
    product_id = input("Enter product id to remove from cart: ")
    found = False
    for item in cart:
        if item['product_id'] == product_id:
            found = True
            confirmation: str = input("Do you really want to remove this product? yes/no: ").lower().strip()
            if confirmation == "yes":
                cart.remove(item)
                storage.save_cart(cart)
                print(f"product removed from cart successfully")
                return
            elif confirmation == "no":
                print("canceled delitation")
                return
            else:
                print("please choose option in yes/no")

    if not found:
        print("no product found from that ID")

def view_cart():
    cart = storage.load_cart()
    if not cart:
        print("Your cart is empty")
        return
    count = 1
    for item in cart:
        print("=" * 50)
        print(f"item count: #{count}")
        print("=" * 50)
        print(f"product ID: {item['product_id']}")
        print(f"product name: {item['product name']}")
        print(f"product price: ₹{item['price']}")
        print(f"product quantity: {item['quantity']}")
        print("=" * 50)
        count += 1


def total_cart():
    cart = storage.load_cart()
    if not cart:
        print("Your cart is empty")
        return

    total = 0 
    for item in cart:
        total += item["price"] * item["quantity"]
    print("=" * 50)
    print("      YOUR GRAND TOTAL IS:")
    print(f"           ₹{total}")
    print("=" * 50)


def get_or_create_customers():
    customers = storage.load_customers()

    customer_id = input("Enter your customer ID: ")
    found = False
    for customer in customers:
        if customer['customer_id'] == customer_id:
            found = True
            return customer
    if not found :
        print("Customer not found. let's create a new customer.")
        name = input("Enter customer name: ")
        email = input("Enter customer email: ")
        phone = input("Enter customer phone: ")
        address = input("Enter customer address: ")

        customer = {
            "customer_id": customer_id,
            "customer_name": name,
            "email": email,
            "phone": phone,
            "address": address
            }

        customers.append(customer)
        storage.save_customers(customers)
        return customer
        
