#!/usr/bin/env python3
'''
Asynch Generator
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """func that generates a random number"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
