#!/usr/bin/env python3
"""Function that takes in a float as an argument
and returns a function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies by the argument"""
    return lambda x: x * multiplier
