from entities.user import User


class UserRepository:
    def __init__(self):
        self.storage = {
            1: User(id=1, name="Swapno", email="swapno@gmail.com", password="1234"),
            2: User(id=2, name="Alex", email="alex@gmail.com", password="abcd"),
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
