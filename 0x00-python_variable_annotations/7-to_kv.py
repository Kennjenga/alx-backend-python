#!/usr/bin/env python3
'''tuple containing a string and a list of int anfd float'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, float(v ** 2))
