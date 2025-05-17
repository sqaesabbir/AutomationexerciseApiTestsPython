"""User API Object"""

from config.constants import (
    VERIFY_LOGIN_ENDPOINT,
    CREATE_ACCOUNT_ENDPOINT,
    DELETE_ACCOUNT_ENDPOINT,
    UPDATE_ACCOUNT_ENDPOINT,
    GET_USER_DETAIL_ENDPOINT
)
from utils.api_helpers import make_request

class UserAPI:
    @staticmethod
    def create_account(user_data):
        """Create a new user account"""
        return make_request("POST", CREATE_ACCOUNT_ENDPOINT, data=user_data)

    @staticmethod
    def delete_account(email, password):
        """Delete a user account"""
        return make_request(
            "DELETE",
            DELETE_ACCOUNT_ENDPOINT,
            data={"email": email, "password": password}
        )

    @staticmethod
    def verify_login(email, password):
        """Verify login with valid credentials"""
        return make_request(
            "POST",
            VERIFY_LOGIN_ENDPOINT,
            data={"email": email, "password": password}
        )

    @staticmethod
    def verify_login_without_email(password):
        """Try login without email parameter"""
        return make_request(
            "POST",
            VERIFY_LOGIN_ENDPOINT,
            data={"password": password}
        )

    @staticmethod
    def verify_login_invalid_method():
        """Try invalid method on login endpoint"""
        return make_request("DELETE", VERIFY_LOGIN_ENDPOINT)

    @staticmethod
    def update_account(user_data):
        """Update user account details"""
        return make_request("PUT", UPDATE_ACCOUNT_ENDPOINT, data=user_data)

    @staticmethod
    def get_user_detail(email):
        """Get user details by email"""
        return make_request(
            "GET",
            GET_USER_DETAIL_ENDPOINT,
            params={"email": email}
        ) 