import storage

def report():
    print("""
========================================
            BUSINESS REPORTS
========================================

1. Sales Report
2. Inventory Report
3. Customer Report
4. Profit Report
5. Back to Main Menu

========================================
""")

    user_option = input("Enter your option: ").lower().strip()
    if user_option in ("1", "sales report"):
        sales_report()
    elif user_option in ("2", "inventory report"):
        inventory_report()
    elif user_option in ("3", "customer report"):
        customer_report()
    elif user_option in ("4", "profit report"):
        profit_report()
    elif user_option in ("5", "back to main menu"):
        return
    else:
        print("Invalid option.")
        


def sales_report():
    orders = storage.load_orders()
    if not orders:
        print("No sales found.")
        return
    
    total_orders = len(orders)
    total_revenue = 0
    total_unit = 0
    for order in orders:
        revenue = order['total_amount']
        total_revenue += revenue
        
        for item in order["items"]:
            sold_quantity = item["quantity"]
            total_unit += sold_quantity

    avg_order_value = total_revenue / total_orders
        

    print(f"""
        ========================================
                    SALES REPORT
        ========================================

            Total Orders       : {total_orders}
            Total Units Sold   : {total_unit}
            Total Revenue      : ₹{total_revenue}
            Average Order Value: ₹{avg_order_value}

        ========================================
""")


def inventory_report():
    products = storage.load_products()
    if not products:
        print("No products found.")
        return

    total_products = len(products)
    total_stock_units = 0
    low_stock_units = 0
    out_of_stock = 0
    total_inventory_value = 0

    for product in products:
        total = product["stock quantity"]
        total_stock_units += total

        total_price = product["purchase price"] * product["stock quantity"]
        total_inventory_value += total_price

        if product["stock quantity"] <= product["minimum stock"]:
            low_stock_units += 1

        if product["stock quantity"] == 0:
            out_of_stock += 1
            


    print(f"""
        ========================================
                  INVENTORY REPORT
        ========================================

        Total Products        : {total_products}
        Total Stock Units     : {total_stock_units}
        Low Stock Products    : {low_stock_units}
        Out-of-Stock Products : {out_of_stock}
        Total Inventory Value : ₹{total_inventory_value}

        ========================================
""")


def customer_report():
    orders = storage.load_orders()
    customers = storage.load_customers()

    total_customers = len(customers)
    total_orders = len(orders)

    active_customers = set()
    total_unit_purchased = 0
    total_customer_spend = 0

    for order in orders:
        active_customers.add(order["customer_id"])
        for item in order["items"]:
            total_unit_purchased += item["quantity"]
            total_customer_spend += item["price"] * item["quantity"]
    active_customers = len(active_customers)

    print(f"""
        ========================================
                    CUSTOMER REPORT
        ========================================

        Total Customers       : {total_customers}
        Customers With Orders : {active_customers}
        Total Orders          : {total_orders}
        Total Units Purchased : {total_unit_purchased}
        Total Customer Spend  : ₹{total_customer_spend}

        ========================================

        """)


def profit_report():
    products = storage.load_products()
    orders = storage.load_orders()

    if not orders:
        print("No sales found.")
        return

    total_orders = len(orders)

    total_units = 0
    total_revenue = 0
    total_cost = 0

    for order in orders:
        for item in order["items"]:
            revenue = item["price"] * item["quantity"]
            total_revenue += revenue
            total_units += item["quantity"]
            for product in products:
                if product["product id"] == item["product_id"]:
                    total_cost += product["purchase price"] * item["quantity"]

    total_profit = total_revenue - total_cost
    if total_revenue > 0:
        profit_margin = (total_profit / total_revenue) * 100
    else:
        profit_margin = 0







    print(f"""
    ========================================
             PROFIT REPORT
    ========================================

    Total Orders        : {total_orders}
    Total Units Sold    : {total_units}
    Total Revenue       : ₹{total_revenue}
    Total Cost          : ₹{total_cost}
    Total Profit        : ₹{total_profit}
    Profit Margin       : {profit_margin}%

    ========================================
    """)