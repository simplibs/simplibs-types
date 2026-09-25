from typing import Annotated
from simplibs.rules import greater_than


int_float_positive = Annotated[int | float, greater_than(0)]
"""Validated type for a positive number (int or float, strictly greater
than zero).

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `int` or `float`.
    2. Value must be strictly greater than 0.

Example:
    @validate_call
    def process(value: int_float_positive): ...
"""