"""Tests for User Operations APIs"""

import pytest
from config.constants import TEST_USER, INVALID_USER, generate_unique_email
from api_objects.user_api import UserAPI
from utils.api_helpers import validate_response

@pytest.fixture
def test_user():
    """Fixture to create unique test user data"""
    user_data = TEST_USER.copy()
    user_data["email"] = generate_unique_email()
    return user_data

@pytest.fixture
def create_test_user(test_user):
    """Fixture to create a test user"""
    response = UserAPI.create_account(test_user)
    validate_response(response, 201, "User created!")
    yield test_user
    # Cleanup: Delete the test user
    try:
        UserAPI.delete_account(test_user["email"], test_user["password"])
    except:
        pass  # Ignore cleanup errors

def test_verify_login_valid_details(create_test_user):
    """Test POST request to verify login with valid details"""
    response = UserAPI.verify_login(
        create_test_user["email"],
        create_test_user["password"]
    )
    validate_response(response, 200, "User exists!")

def test_verify_login_without_email():
    """Test POST request to verify login without email parameter"""
    response = UserAPI.verify_login_without_email("test123")
    validate_response(
        response,
        400,
        "Bad request, email or password parameter is missing in POST request."
    )

def test_verify_login_invalid_method():
    """Test DELETE request to verify login (not supported)"""
    response = UserAPI.verify_login_invalid_method()
    validate_response(
        response,
        405,
        "This request method is not supported."
    )

def test_verify_login_invalid_details():
    """Test POST request to verify login with invalid details"""
    response = UserAPI.verify_login(INVALID_USER["email"], INVALID_USER["password"])
    validate_response(response, 404, "User not found!")

def test_create_and_delete_user(test_user):
    """Test user creation and deletion"""
    # Create user
    response = UserAPI.create_account(test_user)
    validate_response(response, 201, "User created!")
    
    # Delete user
    response = UserAPI.delete_account(test_user["email"], test_user["password"])
    validate_response(response, 200, "Account deleted!")

def test_update_user_account(create_test_user):
    """Test PUT request to update user account"""
    updated_user = create_test_user.copy()
    updated_user["name"] = "Updated Name"
    updated_user["company"] = "Updated Company"
    
    response = UserAPI.update_account(updated_user)
    validate_response(response, 200, "User updated!")

def test_get_user_detail(create_test_user):
    """Test GET request to fetch user details"""
    response = UserAPI.get_user_detail(create_test_user["email"])
    validate_response(response, 200)
    
    # Verify user details in response
    user_data = response.json()
    assert "user" in user_data
    assert user_data["user"]["email"] == create_test_user["email"] 