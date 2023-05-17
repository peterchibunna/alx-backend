#!/usr/bin/python3
"""
Module: 4. LFU Caching
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Class: LFUCache cache implementation
    """

    def __init__(self, *args, **kwargs):
        """Initialize super class after initializing child class
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_usage_frequency = []

    def put(self, key, item):
        """Implement a put method
        """
        if None in [key, item]:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                _key = self.keys_usage_frequency[-1][0]
                self.cache_data.pop(_key)
                self.keys_usage_frequency.pop()
                print("DISCARD: {}".format(_key))
            self.cache_data[key] = item
            ins_index = self.keys_usage_frequency.__len__()
            for k, key_freq in enumerate(self.keys_usage_frequency):
                if 0 == key_freq[1]:
                    ins_index = k
                    break
            self.keys_usage_frequency.insert(ins_index, [key, 0])
        else:
            self.cache_data.__setitem__(key, item)
            self.update_usage_frequencies(key)

    def get(self, key):
        """Implement the get method of class
        """
        if key is not None and key in self.cache_data:
            self.update_usage_frequencies(key)
        return self.cache_data.get(key, None)

    def update_usage_frequencies(self, key):
        """Updates the frequency of usage of items in the cache.
        """
        max_positions = []
        mru_freq = 0
        mru_pos = 0
        ins_pos = 0
        for i, key_freq in enumerate(self.keys_usage_frequency):
            if key_freq[0] == key:
                mru_freq = key_freq[1] + 1
                mru_pos = i
                break
            elif len(max_positions) == 0:
                max_positions.append(i)
            elif key_freq[1] < self.keys_usage_frequency[max_positions[-1]][1]:
                max_positions.append(i)
        max_positions.reverse()
        for pos in max_positions:
            if self.keys_usage_frequency[pos][1] > mru_freq:
                break
            ins_pos = pos
        self.keys_usage_frequency.pop(mru_pos)
        self.keys_usage_frequency.insert(ins_pos, [key, mru_freq])
