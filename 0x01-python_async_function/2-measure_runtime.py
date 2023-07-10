#!/usr/bin/env python3
"""Measures runtime of a function"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures total execution time for wait_n function"""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    stop = time.perf_counter()
    total_time = stop - start

    return total_time / n
