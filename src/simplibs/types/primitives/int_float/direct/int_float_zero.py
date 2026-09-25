from typing import Annotated
from simplibs.rules import is_zero


int_float_zero = Annotated[int | float, is_zero]
"""Validated type for a number (int or float) equal to zero.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `int` or `float`.
    2. Value must be equal to 0.

Example:
    @validate_call
    def process(value: int_float_zero): ...
"""