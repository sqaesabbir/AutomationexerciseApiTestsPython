"""Brands API Object"""

from config.constants import BRANDS_LIST_ENDPOINT
from utils.api_helpers import make_request

class BrandsAPI:
    @staticmethod
    def get_all_brands():
        """Get all brands list"""
        return make_request("GET", BRANDS_LIST_ENDPOINT)

    @staticmethod
    def put_to_brands_list():
        """Try PUT request to brands list (not supported)"""
        return make_request("PUT", BRANDS_LIST_ENDPOINT) 