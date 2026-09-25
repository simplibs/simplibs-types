from typing import Annotated
from simplibs.rules import in_range


int_percentage = Annotated[int, in_range(0, 100)]
"""Validated type for an integer representing a percentage.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `int`.
    2. Value must lie within the inclusive range [0, 100].

Example:
    @validate_call
    def process(value: int_percentage): ...
"""