"""Tests for Products and Brands APIs"""

import pytest
from config.constants import SEARCH_PRODUCTS
from api_objects.products_api import ProductsAPI
from api_objects.brands_api import BrandsAPI
from utils.api_helpers import validate_response

def test_get_all_products():
    """Test GET request to fetch all products"""
    response = ProductsAPI.get_all_products()
    validate_response(response, 200)
    
    # Verify response contains products list
    response_data = response.json()
    assert "products" in response_data
    assert isinstance(response_data["products"], list)

def test_post_to_products_list():
    """Test POST request to products list (not supported)"""
    response = ProductsAPI.post_to_products_list()
    validate_response(
        response,
        405,
        "This request method is not supported."
    )

def test_get_all_brands():
    """Test GET request to fetch all brands"""
    response = BrandsAPI.get_all_brands()
    validate_response(response, 200)
    
    # Verify response contains brands list
    response_data = response.json()
    assert "brands" in response_data
    assert isinstance(response_data["brands"], list)

def test_put_to_brands_list():
    """Test PUT request to brands list (not supported)"""
    response = BrandsAPI.put_to_brands_list()
    validate_response(
        response,
        405,
        "This request method is not supported."
    )

@pytest.mark.parametrize("search_term", SEARCH_PRODUCTS)
def test_search_product(search_term):
    """Test POST request to search products"""
    response = ProductsAPI.search_product(search_term)
    validate_response(response, 200)
    
    # Verify response contains searched products
    response_data = response.json()
    assert "products" in response_data
    assert isinstance(response_data["products"], list)

def test_search_product_without_parameter():
    """Test POST request to search products without search parameter"""
    response = ProductsAPI.search_product_without_param()
    validate_response(
        response,
        400,
        "Bad request, search_product parameter is missing in POST request."
    ) 