"""Constants for API Testing"""

import uuid
from datetime import datetime

# Base URL
BASE_URL = "https://automationexercise.com/api"

# API Endpoints
PRODUCTS_LIST_ENDPOINT = f"{BASE_URL}/productsList"
BRANDS_LIST_ENDPOINT = f"{BASE_URL}/brandsList"
SEARCH_PRODUCT_ENDPOINT = f"{BASE_URL}/searchProduct"
VERIFY_LOGIN_ENDPOINT = f"{BASE_URL}/verifyLogin"
CREATE_ACCOUNT_ENDPOINT = f"{BASE_URL}/createAccount"
DELETE_ACCOUNT_ENDPOINT = f"{BASE_URL}/deleteAccount"
UPDATE_ACCOUNT_ENDPOINT = f"{BASE_URL}/updateAccount"
GET_USER_DETAIL_ENDPOINT = f"{BASE_URL}/getUserDetailByEmail"

def generate_unique_email():
    """Generate a unique email address for testing"""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    unique_id = str(uuid.uuid4())[:8]
    return f"testuser_{timestamp}_{unique_id}@example.com"

# Test Data
TEST_USER = {
    "name": "Test User",
    "email": generate_unique_email(),
    "password": "test123",
    "title": "Mr",
    "birth_date": "1",
    "birth_month": "1",
    "birth_year": "1990",
    "firstname": "Test",
    "lastname": "User",
    "company": "Test Company",
    "address1": "123 Test St",
    "address2": "Apt 4",
    "country": "United States",
    "zipcode": "12345",
    "state": "Test State",
    "city": "Test City",
    "mobile_number": "1234567890"
}

INVALID_USER = {
    "email": "nonexistent@example.com",
    "password": "wrongpass"
}

SEARCH_PRODUCTS = ["top", "tshirt", "jean"] 