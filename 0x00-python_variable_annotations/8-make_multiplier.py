#!/usr/bin/env python3
"""
Task 8 module
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Type-Annotated Multiplier Function Generator for Floating-Point Numbers
    """
    return lambda x: x * multiplier
