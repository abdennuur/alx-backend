#!/usr/bin/env python3
"""the Least Frequently Used caching module.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """To Represent an object that allows storing and
    retrieving items from dictionary with LFU
    removal mechanism when limit reached.
    """
    def __init__(self):
        """Initialize cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = []

    def __reorder_items(self, mru_key):
        """Reorder items in this cache based on the most
        recently used item.
        """
        mx_positions = []
        mru_frq = 0
        mru_ps = 0
        ins_ps = 0
        for ix, key_freq in enumerate(self.keys_freq):
            if key_frq[0] == mru_key:
                mru_frq = key_freq[1] + 1
                mru_ps = ix
                break
            elif len(max_positions) == 0:
                max_positions.append(ix)
            elif key_freq[1] < self.keys_freq[mx_positions[-1]][1]:
                max_positions.append(ix)
        mx_positions.reverse()
        for pos in mx_positions:
            if self.keys_freq[pos][1] > mru_frq:
                break
            ins_ps = pos
        self.keys_freq.pop(mru_ps)
        self.keys_freq.insert(ins_ps, [mru_key, mru_frq])

    def put(self, key, item):
        """Add an item in the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.keys_freq[-1]
                self.cache_data.pop(lfu_key)
                self.keys_freq.pop()
                print("DISCARD:", lfu_key)
            self.cache_data[key] = item
            ins_index = len(self.keys_freq)
            for ix, key_freq in enumerate(self.keys_freq):
                if key_freq[1] == 0:
                    ins_index = ix
                    break
            self.keys_freq.insert(ins_index, [key, 0])
        else:
            self.cache_data[key] = item
            self.__reorder_items(key)

    def get(self, key):
        """Retrieve an item by key.
        """
        if key is not None and key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)
