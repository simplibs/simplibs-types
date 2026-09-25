from typing import Annotated
from simplibs.rules import greater_than


int_positive = Annotated[int, greater_than(0)]
"""Validated type for a positive integer (strictly greater than zero).

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `int`.
    2. Value must be strictly greater than 0.

Example:
    @validate_call
    def process(value: int_positive): ...
"""