#!/usr/bin/env python3
"""
Task 9 module
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Type Annotation for Function Parameters and Return Values
    """
    return [(i, len(i)) for i in lst]
