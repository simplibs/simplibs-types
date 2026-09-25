from typing import Annotated
from simplibs.rules import greater_or_equal


float_non_negative = Annotated[float, greater_or_equal(0.0)]
"""Validated type for a non-negative float (zero or positive).

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `float`.
    2. Value must be greater than or equal to 0.0.

Example:
    @validate_call
    def process(value: float_non_negative): ...
"""