from repositories.user import UserRepository, AuthService

user_id = 0
is_logged_in = False
repo = UserRepository()

auth_service = AuthService(repo)


while True:
    if is_logged_in:
        print("\n\n\n===== MENU =====")
        print("1. View Products")
        print("2. Create Order")
        print("3. View Orders")
        print("4. Exit")

    else:
        print("\n\n\n===== MENU =====")
        print("a. Login")
        print("b. Registration")
        print("c. Demo login")
        print("d. Exit")


    choice = input("Enter choice: ")


    if choice =="1":
        print("One chosen")
    elif choice == "d":
        print("Exiting...")
        break
    if choice == "a":
        email = input("Enter Email: ")
        password = input("Enter Password: ")
        message, status = auth_service.login(
            email=email,
            password=password
        )

        # email="swapno@gmail.com",
            # password="1234"
        if status == 200:
            is_logged_in = True
            print(message)
        else:
            print("Login failed!")

    if choice == "c":
        message, status = auth_service.login(
            email="swapno@gmail.com",
            password="1234"
        )
        if status == 200:
            is_logged_in = True
            print(message)
        else:
            print("Login failed!")
    else:
        print("Invalid choice")