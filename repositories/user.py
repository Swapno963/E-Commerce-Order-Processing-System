from interfaces.user import AuthService
from entities.user import User

class UserRepository:
    def __init__(self):
        self.storage = {
            1: User(
                id=1,
                name="Swapno",
                email="swapno@gmail.com",
                password="1234"
            ),
            2: User(
                id=2,
                name="Alex",
                email="alex@gmail.com",
                password="abcd"
            )
        }

    def get_by_id(self, user_id):
        return self.storage.get(user_id)

    def save(self, user):
        self.storage[user.id] = user

    def get_user_by_email(self, email):
        for user in self.storage.values():
            if user.email == email:
                return user

        return None


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


# =========================
# USAGE
# =========================

