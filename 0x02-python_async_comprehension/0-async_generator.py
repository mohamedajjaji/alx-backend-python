#!/usr/bin/env python3
"""
Task 0 module
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous Generator Yielding Random Numbers with Delay
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
