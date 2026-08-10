from model import User


def get_user(user_id: int) -> User:
    return User(user_id, "Dhanush")

def get_user_name(user_id: int) -> str:
    user = get_user(user_id)
    return user.name