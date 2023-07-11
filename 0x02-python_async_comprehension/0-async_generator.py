#!/usr/bin/env python3
"""Create an async generator function"""
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """Generator function that yields values between
    0 to 10 randomly
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
