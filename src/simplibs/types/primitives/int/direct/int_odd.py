from typing import Annotated
from simplibs.rules import is_odd


int_odd = Annotated[int, is_odd]
"""Validated type for an odd integer.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `int`.
    2. Value must be odd (not divisible by 2).

Example:
    @validate_call
    def process(value: int_odd): ...
"""