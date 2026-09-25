from typing import Annotated
from simplibs.rules import negate, is_nan


float_not_nan = Annotated[float, negate(is_nan)]
"""Validated type for a float that is not NaN.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `float`.
    2. Value must not be NaN (negated `is_nan`).

Detailed description:
    Unlike `float_finite`, this only excludes NaN — +/-infinity is still
    accepted. Use `float_finite` if both NaN and infinity should be
    rejected.

Example:
    @validate_call
    def process(value: float_not_nan): ...
"""