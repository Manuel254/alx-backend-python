#!/usr/bin/env python3
"""This module implements Async comprehensions"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Returns a list of random float numbers"""
    return [num async for num in async_generator()]
