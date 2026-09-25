from typing import Annotated
from simplibs.rules import in_range


int_uint8 = Annotated[int, in_range(0, 255)]
"""Validated type for an integer in the unsigned 8-bit range.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `int`.
    2. Value must lie within the inclusive range [0, 255].

Example:
    @validate_call
    def process(value: int_uint8): ...
"""