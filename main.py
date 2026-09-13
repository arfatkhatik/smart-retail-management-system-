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
    5. inventry management
    6. sales & analytics
    7. search
    8. report
    9. setting 
    10.exit

=====================================================================================
""")
import products
user_option = input("enter your choice: ")
while True:
    if user_option in ("1", "product management"):
        products.product_manager()
    break