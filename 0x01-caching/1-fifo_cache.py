#!/usr/bin/python3
"""
Module: 1. FIFO Caching
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Class: FIFO cache implementation
    """
    def __init__(self, *args, **kwargs):
        """Initialize super class after initializing child class
        """
        super().__init__()

    def put(self, key, item):
        """Implement a put method
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
        if self.cache_data.items().__len__() > BaseCaching.MAX_ITEMS:
            deleted_key = list(self.cache_data.items())[0][0]
            del self.cache_data[deleted_key]
            print('DISCARD: {}'.format(deleted_key))

    def get(self, key):
        """Implement the get method of class
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
