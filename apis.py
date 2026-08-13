"""
Feature 02: API layer.

This layer depends on Feature 01 because it uses
the User class defined there.
"""

from model import User


# Simulates retrieving a user from a database.
def get_user(user_id: int) -> User:
    return User(user_id, f"User-{user_id}")


# Converts the User object into an API-style response.
def user_response(user_id: int) -> dict:
    user = get_user(user_id)

    return {
        "id": user.user_id,
        "name": user.name,
    }