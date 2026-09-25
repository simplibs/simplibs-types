from typing import Annotated
from simplibs.rules import is_finite


float_finite = Annotated[float, is_finite]
"""Validated type for a finite float (neither NaN nor infinite).

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `float`.
    2. Value must be finite (not NaN and not +/-infinity).

Example:
    @validate_call
    def process(value: float_finite): ...
"""