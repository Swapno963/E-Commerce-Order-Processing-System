from repositories.user import UserRepository
from repositories.product import ProductRepository
from services.user import AuthService
from services.product import ProductService

user_id = 0
is_logged_in = False
auth_repo = UserRepository()
product_repo = ProductRepository()

auth_service = AuthService(auth_repo)
product_service = ProductService(product_repo)


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

    elif choice == "e":
        print("Exiting...")
        break
    if choice == "a":
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

    if choice == "c":
        message, status = auth_service.login(email="swapno@gmail.com", password="1234")
        if status == 200:
            is_logged_in = True
            print(message)
        else:
            print("Login failed!")
    else:
        print("Invalid choice")
