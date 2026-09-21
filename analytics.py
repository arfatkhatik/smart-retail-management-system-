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