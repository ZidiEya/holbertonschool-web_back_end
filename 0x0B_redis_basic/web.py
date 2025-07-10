#!/usr/bin/env python3
"""
Web caching and access counter with decorators
"""

import redis
import requests
from functools import wraps

r = redis.Redis()


def count_access(func):
    """Decorator to count how many times a URL is accessed"""
    @wraps(func)
    def wrapper(url):
        r.incr(f"count:{url}")
        return func(url)
    return wrapper


def cache_page(expiration=10):
    """Decorator to cache a page for a given number of seconds"""
    def decorator(func):
        @wraps(func)
        def wrapper(url):
            cache_key = f"cache:{url}"
            cached = r.get(cache_key)
            if cached:
                return cached.decode('utf-8')
            result = func(url)
            r.setex(cache_key, expiration, result)
            return result
        return wrapper
    return decorator


@count_access
@cache_page(10)
def get_page(url: str) -> str:
    """
    Fetch a web page with caching and access tracking
    """
    return requests.get(url).text
