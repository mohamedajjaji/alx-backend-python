#!/usr/bin/env python3
"""
Task 6 module
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Type-Annotated Mixed List Summation Function for Integers and Floats
    """
    return float(sum(mxd_lst))
