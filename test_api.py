from api import get_user


def get_user_name(user_id: int) -> str:
    user = get_user(user_id)
    return user.name.upper()