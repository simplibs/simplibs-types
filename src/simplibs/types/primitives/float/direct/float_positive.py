from typing import Annotated
from simplibs.rules import greater_than


float_positive = Annotated[float, greater_than(0.0)]
"""Validated type for a positive float (strictly greater than zero).

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `float`.
    2. Value must be strictly greater than 0.0.

Example:
    @validate_call
    def process(value: float_positive): ...
"""