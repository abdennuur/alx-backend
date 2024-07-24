#!/usr/bin/env python3
"""The basic caching module.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """To represent object that allows storing and
    retrievs items frm a dictionary.
    """
    def put(self, key, item):
        """Adds item in cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """To retrieve an item by key.
        """
        return self.cache_data.get(key, None)
