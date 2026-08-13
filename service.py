"""
Feature 05: service layer.

This is the top layer of our POC and depends on
the validation/API layers below it.
"""

from validation import get_validated_user


# Builds a human-readable user summary.
def build_user_summary(user_id: int) -> str:

    user = get_validated_user(user_id)

    return f"User {user['id']}: {user['name']}"


# Convenience function using a default user.
def build_default_summary() -> str:
    return build_user_summary(1)