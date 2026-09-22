import storage

def sales_manager():
    print("""
    ========================================
          SALES & ANALYTICS
    ========================================

        1. Sales Overview
        2. Product Sales
        3. Category Sales
        4. Customer Analytics
        5. Profit Analytics
        6. Back to Main Menu

    ========================================
""")
    user_option = input("Enter your option: ").lower().strip()
    if user_option in ("1", "sales overview"):
        sales_overview()
    elif user_option in ("2", "product sales"):
        products_sales()
    elif user_option in ("3", "category sales"):
        category_sales()

def sales_overview():
    orders = storage.load_orders()

    if not orders:
        print("No order found.")
        return

    total_revenue = 0 
    total_unit = 0

    for order in orders:
        total_revenue += order['total_amount']
        for item in order["items"]:
            total_unit += item['quantity']

    total_orders = len(orders)
    average_order = total_revenue / total_orders

    print("=" * 50)
    print("         SALES OVERVIEW")
    print("=" * 50)
    print(f"Total order: {total_orders}")
    print(f"Total revenue: {total_revenue}")
    print(f"total unit sold: {total_unit}")
    print(f"average order value: {average_order}")
    print("=" * 50)


def products_sales():
    orders = storage.load_orders()
    if not orders:
        print("No order found.")
        return

    product_sales_data = {}
    for order in orders:
        for item in order["items"]:
            product_id = item["product_id"]

            if product_id not in product_sales_data:
                product_sales_data[product_id] = {
                    "product_name": item["product name"],
                    "quantity": 0,
                    "revenue": 0
                }
            product_sales_data[product_id]['quantity'] += item["quantity"]
            sale_amount = item["price"] * item["quantity"]
            product_sales_data[product_id]["revenue"] += (
                sale_amount
            )
    print("=" * 50)
    print("             PRODUCT SALES")
    print("=" * 50)

    for product_id, data in product_sales_data.items():
        print(f"Product ID: {product_id}")
        print(f"Product Name: {data['product_name']}")
        print(f"Units Sold: {data['quantity']}")
        print(f"Revenue: ₹{data['revenue']}")
        print("-" * 50)


def category_sales():
    orders = storage.load_orders()
    if not orders:
        print("No order found.")
        return
    products = storage.load_products()
    category_sales_data = {}
    for order in orders:
        for item in order["items"]:
            for product in products:
                if product["product id"] == item["product_id"]:
                    category = product["category"]
                    if category not in category_sales_data:
                        category_sales_data[category] = {
                            "quantity": 0,
                            "revenue": 0
                        }
                    category_sales_data[category]["quantity"] += item["quantity"]
                    category_sales_data[category]["revenue"] += (
                        item["price"] * item["quantity"]
                    )
                    break
    print("=" * 50)
    print("         CATEGORY SALES")
    print("=" * 50)
    for category, data in category_sales_data.items():
        print(f"category: {category}")
        print(f"Units Sold: {data['quantity']}")
        print(f"Revenue: ₹{data['revenue']}")
        print("-" * 50)
