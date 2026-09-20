import storage

def create_order():
    customer_id = input("Enter customer ID: ")
    cart = storage.load_cart()
    customer_cart = None 

    for saved_cart in cart:
        if saved_cart.get('customer_id') == customer_id:
            customer_cart = saved_cart
            break

    if customer_cart is None:
        print("No cart found for this customer.")
        return

    if not customer_cart["items"]:
        print("Your cart is empty.")
        return

    total_amount = 0

    for item in customer_cart["items"]:
        total_amount += item["price"] * item["quantity"]
        

    print("=" * 25 + "[ ORDER SUMMARY ]" + "=" * 25)

    for item in customer_cart["items"]:
        print(f"product: {item['product name']}")
        print(f"price: ₹{item['price']} ")
        print(f"quantity: {item['quantity']}")
        print(f"subtotal: ₹{item['price']} * {item['quantity']}")
        print("-" * 30)

    print(f"TOTAL AMOUNT: ₹{total_amount} ")
    print("=" * 67)
    confirmation = input("confirm order? yes/no: ").lower().strip()

    if confirmation == "no":
        print("order cancelled.")
        return
    elif confirmation != "yes":
        print("Invalid option.")
        return
    elif confirmation == "yes":
        orders = storage.load_orders()
        order_number = len(orders) + 1
        order_id = f"o0{order_number}"

        order = {
        "order_id": order_id,
        "customer_id": customer_id,
        "items": customer_cart["items"],
        "total_amount": total_amount,
        "status": "Confirmed"
        }

        products = storage.load_products()
        for item in customer_cart["items"]:
            for product in products:
                if product['product id'] == item['product_id']:
                    product['stock quantity'] -= item['quantity']
                    break
        storage.save_products(products)
        orders.append(order)
        storage.save_order(orders)
            

        print("Order placed successfully.")

        customer_cart["items"] = []
        storage.save_cart(cart)
