"""
Feature 03: validation layer.

This depends on Feature 02 because it calls
the API response function from Feature 02.
"""

from apis import user_response


# Check whether the user ID is valid.
def validate_user_id(user_id: int) -> bool:
    return isinstance(user_id, int) and user_id > 0


# Only call the API after validation succeeds.
def get_validated_user(user_id: int) -> dict:

    if not validate_user_id(user_id):
        raise ValueError("user_id must be a positive integer")

    return user_response(user_id)