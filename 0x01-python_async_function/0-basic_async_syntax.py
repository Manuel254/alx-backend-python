#!/usr/bin/env python3
"""This module creates a coroutine that waits for a random
delat between 0 and max_delay and eventually returns it
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Coroutine that waits for a random delay
    and returns the delay
    """
    return random.uniform(0, max_delay)
