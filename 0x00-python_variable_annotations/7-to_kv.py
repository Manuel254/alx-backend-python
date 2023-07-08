#!/usr/bin/env python3
"""Function that takes a string string k 
and an int OR float v as arguments and returns a tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return Tuple"""
    return (k, v ** 2)
