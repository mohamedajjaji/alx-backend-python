#!/usr/bin/env python3
"""
Task 10 module
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    First Element Retrieval from Sequence (If Exists)
    """
    if lst:
        return lst[0]
    else:
        return None
