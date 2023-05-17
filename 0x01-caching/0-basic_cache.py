#!/usr/bin/python3
"""
Module basic cache
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache module
    """

    def put(self, key, item):
        """Implement the put method of class
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Implement the get method of class
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
