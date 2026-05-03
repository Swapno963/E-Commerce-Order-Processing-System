from interfaces.user import AuthService


class AuthService(AuthService):
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def login(self, email, password):
        user = self.user_repo.get_user_by_email(email)

        if not user:
            raise Exception("User not found")

        if user.password != password:
            raise Exception("Invalid password")

        return f"Welcome {user.name}", 200
