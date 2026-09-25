from typing import Annotated
from simplibs.rules import in_range


float_percentage = Annotated[float, in_range(0.0, 100.0)]
"""Validated type for a float representing a percentage.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `float`.
    2. Value must lie within the inclusive range [0.0, 100.0].

Example:
    @validate_call
    def process(value: float_percentage): ...
"""