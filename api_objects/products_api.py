"""Products API Object"""

from config.constants import PRODUCTS_LIST_ENDPOINT, SEARCH_PRODUCT_ENDPOINT
from utils.api_helpers import make_request

class ProductsAPI:
    @staticmethod
    def get_all_products():
        """Get all products list"""
        return make_request("GET", PRODUCTS_LIST_ENDPOINT)

    @staticmethod
    def post_to_products_list():
        """Try POST request to products list (not supported)"""
        return make_request("POST", PRODUCTS_LIST_ENDPOINT)

    @staticmethod
    def search_product(search_term):
        """Search for products"""
        return make_request(
            "POST",
            SEARCH_PRODUCT_ENDPOINT,
            data={"search_product": search_term}
        )

    @staticmethod
    def search_product_without_param():
        """Search products without required parameter"""
        return make_request("POST", SEARCH_PRODUCT_ENDPOINT) 