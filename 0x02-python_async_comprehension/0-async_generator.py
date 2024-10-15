#!/usr/bin/env python3

""" Async Comprehensions """

import asyncio
from random import uniform
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    for _ in range(10):
        await asyncio.sleep(1)  # Use await for asyncio.sleep
        yield uniform(0, 10)
