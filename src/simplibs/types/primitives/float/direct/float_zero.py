from typing import Annotated
from simplibs.rules import is_zero


float_zero = Annotated[float, is_zero]
"""Validated type for a float equal to zero.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `float`.
    2. Value must be equal to 0.

Example:
    @validate_call
    def process(value: float_zero): ...
"""