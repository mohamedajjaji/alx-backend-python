#!/usr/bin/env python3
"""
Task 7 module
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Type-Annotated Key-Value Squaring Function for Strings and Integers/Floats
    """
    return (k, float(v**2))
