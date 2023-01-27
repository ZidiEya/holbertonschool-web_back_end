#!/usr/bin/env python3
'''func to create a class BasicCache that inherits
from BaseCaching and is a caching system:'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    ''' must use self.cache_data - dictionary
    from the parent class BaseCaching This
    caching system doesn’t have limit'''
    def put(self, key, item):
        '''must assign to the dictionary self.cache_data
        the item value for the key key. If key or item
        is None, this method should not do anything'''
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        '''must return the value in self.cache_data
        linked to key. If key is None or if the key
        doesn’t exist in self.cache_data, return None.'''
        return self.cache_data.get(key)
