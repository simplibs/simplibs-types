from typing import Annotated
from simplibs.rules import greater_or_equal, is_even


int_non_negative_even = Annotated[int, greater_or_equal(0) & is_even]
"""Validated type for a non-negative, even integer.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `int`.
    2. Value must be greater than or equal to 0.
    3. Value must be even.

Example:
    @validate_call
    def process(value: int_non_negative_even): ...
"""