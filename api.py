from model import User


def get_user(user_id: int) -> User:
    return User(user_id, "Dhanush")