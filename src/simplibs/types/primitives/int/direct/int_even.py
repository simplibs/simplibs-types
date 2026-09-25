from typing import Annotated
from simplibs.rules import is_even


int_even = Annotated[int, is_even]
"""Validated type for an even integer.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `int`.
    2. Value must be even (divisible by 2).

Example:
    @validate_call
    def process(value: int_even): ...
"""