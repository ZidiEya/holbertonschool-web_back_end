#!/usr/bin/env python3
""" BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache defines a caching system without limit.
    It stores items in a dictionary and retrieves them by key.
    """

    def put(self, key, item):
        """Add an item in the cache.

        Args:
            key: The key under which to store the item.
            item: The value to store.

        If key or item is None, this method does nothing.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item by key.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The value linked to the key, or None if key is None
            or if key does not exist in cache_data.
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
