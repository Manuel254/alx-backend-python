#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the performance of four parallel
    asynchronous comprehensions
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    stop = time.perf_counter()
    return stop - start
