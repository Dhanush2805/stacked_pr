"""
Feature 04: tests.

These tests depend on Feature 03 because they test
the validation layer.
"""

from validation import validate_user_id, get_validated_user


# Valid IDs should pass validation.
def test_valid_user_id():
    assert validate_user_id(10) is True


# Zero should fail validation.
def test_invalid_user_id():
    assert validate_user_id(0) is False


# Verify that the API response still works through validation.
def test_user_response():
    response = get_validated_user(10)

    assert response["id"] == 10