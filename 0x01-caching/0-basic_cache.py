#!/usr/bin/python3
"""
Module basic cache
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache module
    """

    def put(self, key, item):
        if key is not None:
            self.cache_data[key] = item
        """Implement the put method of class
        """

    def get(self, key):
        """Implement the get method of class
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
