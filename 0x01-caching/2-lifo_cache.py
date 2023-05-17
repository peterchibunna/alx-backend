#!/usr/bin/python3
"""
Module: 1. LIFO Caching
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Class: LIFOCache cache implementation
    """
    def __init__(self, *args, **kwargs):
        """Initialize super class after initializing child class
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Implement a put method
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)
        if self.cache_data.items().__len__() > BaseCaching.MAX_ITEMS:
            items_size = BaseCaching.MAX_ITEMS
            deleted_key = list(self.cache_data.items())[items_size - 1][0]
            del self.cache_data[deleted_key]
            print('DISCARD: {}'.format(deleted_key))

    def get(self, key):
        """Implement the get method of class
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
