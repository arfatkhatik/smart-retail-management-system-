print("""
====================================================================================

                              SMART RETAIL MANAGEMENT
                                    SYSTEM

=====================================================================================


                              business management

                          • products • customers • orders

                          • inventry • sales • reports

                          
                                version 1.0

                           devloped by arfat khatik


------------------------------------------------------------------------------------

                               SYSTEM STARTING...

------------------------------------------------------------------------------------
""")
input(                   "Press ENTER to continue...")
print("""
====================================================================================

                               MAIN MENU

=====================================================================================

    1. product management
    2. customer management
    3. shopping cart
    4. order management
    5. inventory management
    6. sales & analytics
    7. search
    8. report
    9. setting 
    10.exit

=====================================================================================
""")
import products
import customers
import cart
import orders
import inventory
while True:
    user_option = input("enter your choice: ")
    if user_option in ("1", "product management"):
        products.product_manager()
    elif user_option in ("2", "customer management"):
        customers.customer_manager()
    elif user_option in ("3", "shopping cart"):
        cart.cart_manager()
    elif user_option in ("4", "order managemenr"):
        orders.create_order()
    elif user_option in ("5", "inventory management"):
        inventory.inventry_manager()
    
            
            
    break