from model import User


def get_user(user_id: int) -> User:
    return User(user_id, "Dhanush", "email")

def get_user_name(user_id: int) -> str:
    user = get_user(user_id)
    return f"User: {user.name}"

x=get_user_name(1)
print(x)