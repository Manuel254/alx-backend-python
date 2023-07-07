#!/usr/bin/env python3
"""This module implements a function that accepts a
a list of floats and returns their sum as a float
"""
from functools import reduce
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Calculates sum of floats in a list"""
    return reduce(lambda a, b: a + b, input_list)
