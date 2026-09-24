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