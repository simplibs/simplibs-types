from typing import Annotated
from simplibs.rules import is_finite


int_float_finite = Annotated[int | float, is_finite]
"""Validated type for a finite number (int or float, neither NaN nor
infinite).

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `int` or `float`.
    2. Value must be finite (not NaN and not +/-infinity).

Detailed description:
    Relevant mainly for the `float` case, since plain `int` values are
    always finite by construction — this rule is what makes `int_float_finite`
    meaningfully stricter than the bare `Number` type when a `float` is
    passed.

Example:
    @validate_call
    def process(value: int_float_finite): ...
"""