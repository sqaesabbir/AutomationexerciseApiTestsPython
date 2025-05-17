"""Helper functions for API testing"""

import requests
from typing import Dict, Any, Optional

def make_request(
    method: str,
    url: str,
    params: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None
) -> requests.Response:
    """
    Make an HTTP request to the specified URL
    
    Args:
        method: HTTP method (GET, POST, PUT, DELETE)
        url: API endpoint URL
        params: URL parameters (optional)
        data: Request body data (optional)
    
    Returns:
        requests.Response object
    """
    method = method.upper()
    
    if method == "GET":
        response = requests.get(url, params=params)
    elif method == "POST":
        response = requests.post(url, data=data)
    elif method == "PUT":
        response = requests.put(url, data=data)
    elif method == "DELETE":
        response = requests.delete(url, data=data)
    else:
        raise ValueError(f"Unsupported HTTP method: {method}")
    
    return response

def validate_response(
    response: requests.Response,
    expected_status_code: int,
    expected_message: Optional[str] = None
) -> None:
    """
    Validate the API response
    
    Args:
        response: Response object from the API
        expected_status_code: Expected status code (either HTTP or response code)
        expected_message: Expected response message (optional)
    """
    # First check if response can be parsed as JSON
    try:
        response_data = response.json()
    except ValueError:
        response_data = {}
    
    # For this API, all successful responses have HTTP 200 status code
    # and the actual status code is in the responseCode field
    assert response.status_code == 200, \
        f"Expected HTTP status code 200, but got {response.status_code}"
    
    # Check the response code in the body
    if "responseCode" in response_data:
        actual_status_code = response_data["responseCode"]
        assert actual_status_code == expected_status_code, \
            f"Expected response code {expected_status_code}, but got {actual_status_code}"
    
    if expected_message:
        assert "message" in response_data, "Response does not contain a message field"
        actual_message = response_data["message"]
        assert actual_message == expected_message, \
            f"Expected message '{expected_message}', but got '{actual_message}'" 