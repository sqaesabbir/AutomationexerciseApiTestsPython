"""Debug tests to check actual API responses"""

import json
from api_objects.products_api import ProductsAPI
from api_objects.user_api import UserAPI
from config.constants import TEST_USER

def test_debug_create_user():
    """Debug test to check create user response"""
    print("\nCreate User Request:")
    print("URL:", UserAPI.create_account.__doc__)
    print("Data:", json.dumps(TEST_USER, indent=2))
    
    response = UserAPI.create_account(TEST_USER)
    print("\nCreate User Response:")
    print(f"Status Code: {response.status_code}")
    print("Headers:", dict(response.headers))
    print("Response Body:", response.text)
    
    # Print the actual error message if present
    try:
        response_data = response.json()
        if "message" in response_data:
            print("\nError Message:", response_data["message"])
    except ValueError:
        print("Could not parse response as JSON")

def test_debug_post_products():
    """Debug test to check POST products response"""
    response = ProductsAPI.post_to_products_list()
    print("\nPOST Products Response:")
    print(f"Status Code: {response.status_code}")
    print("Response Body:", response.text) 