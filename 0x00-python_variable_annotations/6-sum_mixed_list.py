#!/usr/bin/env python3
"""This module contains a function which takes a list of mixed integers
and floats and returns their sum as a float
"""
from typing import List, Union
from functools import reduce


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum as float"""
    return reduce(lambda a, b: a + b, mxd_lst)
