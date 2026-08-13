"""
Feature 01: User model.

This is the foundation of our demo.
Later features will depend on this User model.
"""


class User:
    # Constructor: creates a User object.
    def __init__(self, user_id: int, name: str):
        self.user_id = user_id
        self.name = name

    # Returns a simple display name.
    def display_name(self) -> str:
        return f"{self.user_id}: {self.name}"


# Helper function used by future layers.
def create_user(user_id: int, name: str) -> User:
    return User(user_id, name)