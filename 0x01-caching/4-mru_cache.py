#!/usr/bin/python3
"""
Module: 4. MRU Caching
"""
from collections import OrderedDict

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Class: MRUCache cache implementation
    """
    def __init__(self, *args, **kwargs):
        """Initialize super class after initializing child class
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Implement a put method
        """
        if None in [key, item]:
            return
        if key in self.cache_data:
            # "key and item exists"
            self.cache_data[key] = item
        else:
            # "key or item is none"
            # if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
            if self.cache_data.items().__len__() + 1 > BaseCaching.MAX_ITEMS:
                items_size = BaseCaching.MAX_ITEMS
                deleted_key = list(self.cache_data.items())[0][0]
                del self.cache_data[deleted_key]
                print('DISCARD: {}'.format(deleted_key))
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """Implement the get method of class
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
