from api import get_user


def test_get_user():
    user = get_user(1)

    assert user.user_id == 1
    assert user.name == "Dhanush"