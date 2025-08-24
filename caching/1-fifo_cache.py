#!/usr/bin/env python3
""" FIFOCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache defines a caching system using FIFO algorithm.
    When the number of items exceeds MAX_ITEMS,
    the oldest item is discarded.
    """

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.queue = []  # To keep track of insertion order

    def put(self, key, item):
        """Add an item in the cache.

        Args:
            key: The key under which to store the item.
            item: The value to store.

        If key or item is None, this method does nothing.
        If the cache exceeds MAX_ITEMS, the oldest item
        is discarded (FIFO) and a message is printed.
        """
        if key is None or item is None:
            return

        # If key already exists, update the value without discarding
        if key in self.cache_data:
            self.cache_data[key] = item
            return

        # If cache is full, remove first inserted (FIFO)
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            oldest_key = self.queue.pop(0)
            del self.cache_data[oldest_key]
            print("DISCARD:", oldest_key)

        self.cache_data[key] = item
        self.queue.append(key)

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
