#!/usr/bin/env python3
"""Execute multiple coroutines at the same time"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of all delays"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    output = [await task for task in asyncio.as_completed(tasks)]
    return output
