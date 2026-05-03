from repositories.user import UserRepository
from repositories.product import ProductRepository
from repositories.order_item import OrderItemRepository
from repositories.order import OrderRepository
from services.user import AuthService
from services.product import ProductService
from services.orderItem import OrderItemService
from services.order import OrderService

user_id = 0
is_logged_in = False
auth_repo = UserRepository()
product_repo = ProductRepository()
order_item_repo = OrderItemRepository()
order_repo = OrderRepository()

auth_service = AuthService(auth_repo)
product_service = ProductService(product_repo)
order_item_service = OrderItemService(order_item_repo)
order_service = OrderService(order_repo)

while True:
    if is_logged_in:
        print("\n\n\n===== MENU =====")
        print("1. View Products")
        print("2. Create Order")
        print("3. View Orders")
        print("e. Exit")

    else:
        print("\n\n\n===== MENU =====")
        print("a. Login")
        print("b. Registration")
        print("c. Demo login")
        print("e. Exit")

    choice = input("Enter choice: ")
    if choice == "1":
        products = product_service.viewAllProducts()
        print("products : ", products)

    elif choice == "2":
        product_id = input("Enter Product id: ")
        quantity = input("Enter how many you want: ")
        new_item = order_item_service.create_order_item(
            id=3, product_id=product_id, quantity=quantity
        )
        new_order = order_service.create_order(id=3, order_item=3, user_id=1)
        print("Created Order:", new_order)

    elif choice == "3":
        orders = order_service.get_all_orders()
        print("Orders", orders)
    elif choice == "e":
        print("Exiting...")
        break
    elif choice == "a":
        email = input("Enter Email: ")
        password = input("Enter Password: ")
        message, status = auth_service.login(email=email, password=password)

        # email="swapno@gmail.com",
        # password="1234"
        if status == 200:
            is_logged_in = True
            print(message)
        else:
            print("Login failed!")

    elif choice == "c":
        message, status = auth_service.login(email="swapno@gmail.com", password="1234")
        if status == 200:
            is_logged_in = True
            print(message)
        else:
            print("Login failed!")
    else:
        print("Invalid choice")
