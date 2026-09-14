import storage

def customer_manager():
    while True:
        print("""
    ======================================================================================

                                CUSTOMER MANAGEMENT

    ======================================================================================

    -----------------------------
            1. Add Customer
            2. View Customers
            3. Search Customer
            4. Update Customer
            5. Delete Customer
            6. cancel / Back to Main Menu
    -----------------------------

    ======================================================================================
""")
        user_option = str(input("Enter your option: "))
        if user_option in ("1", "add customer"):
            add_customer()
        elif user_option in ("2", "view customers"):
            view_customers()
        elif user_option in ("3", "search customer"):
            search_customer()
        elif user_option in ("4", "update customer"):
            update_customer()
        elif user_option in ("5", "delete customer"):
            delete_customer()
        elif user_option in ("6", "cancel", "back to main menu"):
            return
        else:
            print("Invalid option. Please select a valid option.")


def add_customer():
    customers = storage.load_customers()
    found = False
    customer_id = input("Enter customer ID: ")
    customer_name = input("Enter customer name: ")
    customer_email = input("Enter customer email: ")
    customer_phone = int(input("Enter customer phone: "))
    customer_address = input("Enter customer address: ")
    for customer in customers:
        if customer["customer_id"] == customer_id:
            found = True
            break
    if found:
        print("Customer with this ID already exists.")
        return
    customer = {
        "customer_id": customer_id,
        "name": customer_name,
        "email": customer_email,
        "phone": customer_phone,
        "address": customer_address
    }
    customers.append(customer)
    storage.save_customers(customers)
    print("Customer added successfully.")
    return


def view_customers():
    customers = storage.load_customers()
    count = 1
    if not customers:
        print("No customers found.")
    else:
        print("Customer List: ")
        for customer in customers:
            print("=" * 30)
            print(f"Customer        #{count}:")
            print("=" * 30)
            print(f"ID: {customer['customer_id']}")
            print(f"Name: {customer['name']}")
            print(f"Email: {customer['email']}")
            print(f"Phone: {customer['phone']}")
            print(f"Address: {customer['address']}")
            print("=" * 30)
            count += 1
            


def search_customer():
    print("=" * 60)
    print("             SEARCH CUSTOMERS")
    print("=" * 60)
    print("1. search by id")
    print("2. search by name")
    print("3. search by email")
    print("4. search by phone")
    print("5. search by address")
    print("6. back")
    print("=" * 60)
    user_input = input("Enter your option: ")
    if user_input in ("1", "search by id"):
        searchby_id()
    elif user_input in ("2", "search by name"):
        searchby_name()
    elif user_input in ("3", "search by email"):
        searchby_email()
    elif user_input in ("4", "search by phone"):
        searchby_phone()
    elif user_input in ("5", "search by address"):
        searchby_address()
    elif user_input in ("6", "back"):
        return


def _print_customer(customer):
    print("-" * 60)
    print(f"Customer ID:       {customer['customer_id']}")
    print(f"Customer name:     {customer['name']}")
    print(f"Email:             {customer['email']}")
    print(f"Phone:             {customer['phone']}")
    print(f"Address:           {customer['address']}")


def searchby_id():
    customers = storage.load_customers()
    customer_id = input("Enter id to search customer: ")
    found = False
    for customer in customers:
        if customer["customer_id"] == customer_id:
            found = True
            print("customer found")
            _print_customer(customer)
    if not found:
        print("Customer with this id not found.")
            


def searchby_name():
    customers = storage.load_customers()
    customer_name = input("Enter name to search customer: ")
    found = False
    for customer in customers:
        if customer['name'].lower() == customer_name.lower():
            found = True
            print("customer found")
            _print_customer(customer)
    if not found:
        print("customer with this name not found.")
        


def searchby_email():
    customers = storage.load_customers()
    customer_email = input("Enter email to search customer: ").lower().strip()
    found = False
    for customer in customers:
        if customer['email'].lower() == customer_email:
            found = True
            print("customer found")
            _print_customer(customer)
    if not found :
        print("customer with this email not found.")
            


def searchby_phone():
    customers = storage.load_customers()
    customer_phone = int(input("Enter phone number to search customer: "))
    found = False
    for customer in customers:
        if customer['phone'] == customer_phone:
            found = True
            print("customer found")
            _print_customer(customer)
    if not found:
        print("customer with this phone number not found.")
        


def searchby_address():
    customers = storage.load_customers()
    customer_address = input("Enter address to search customer: ")
    found = False
    for customer in customers:
        if customer['address'].lower() == customer_address.lower():
            found = True
            print("customer found")
            _print_customer(customer)
    if not found:
        print("customer with this address not found.")



def update_customer():
    customers = storage.load_customers()
    customer_id = input("Enter customer ID to update: ")
    found = False
    for customer in customers:
        if customer["customer_id"] == customer_id:
            found = True
            print("=" * 60)
            print("             UPDATE CUSTOMER")
            print("=" * 60)
            print("1. update by id")
            print("2. update by name")
            print("3. update by email")
            print("4. update by phone")
            print("5. update by address")
            print("6. back")
            print("=" * 60)
            input_option = input("Enter you option: ")
            if input_option in ("1", "update by id"):
                new_id = input("Enter new customer ID: ")
                customer["customer_id"] = new_id
            elif input_option in ("2", "update by name"):
                new_name = input("Enter new customer name: ")
                customer["name"] = new_name
            elif input_option in ("3", "update by email"):
                new_email = input("Enter new customer email: ")
                customer["email"] = new_email
            elif input_option in ("4", "update by phone"):
                new_phone = int(input("Enter new customer phone: "))    
                customer['phone'] = new_phone
            elif input_option in ("5", "update by address"):   
                new_address = input("Enter new customer address: ")
                customer["address"] = new_address
            elif input_option in ("6", "back"):
                return
            else:
                print("Invalid option. Please select a valid option.")
    if not found:
        print("Customer with this ID not found.")
        return
    storage.save_customers(customers)


def delete_customer():
    customers = storage.load_customers()
    customer_id = input("Enter customer ID to delete: ")
    found = False
    for customer in customers:
        if customer["customer_id"] == customer_id:
            found = True
            confirmation = input(f"Do you really wanted to delete {customer['name']} this customer? (yes/no): ").lower().strip()
            if confirmation == "yes":
                customers.remove(customer)
                storage.save_customers(customers)
                print(f"customer deleted successfully")
                return
            elif confirmation == "no":
                print("Deletion cancelled.")
                return
    if not found:
        print("no customer found with that ID")
        