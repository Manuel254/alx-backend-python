#!/usr/bin/env python3
"""Execute multiple coroutines at the same time"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of all delays"""
    coroutines = [wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*coroutines))
