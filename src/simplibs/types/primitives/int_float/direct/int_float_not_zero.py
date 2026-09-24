from simplibs.validate import validated_type
from simplibs.rules import negate, is_zero


int_float_not_zero = validated_type(int | float, negate(is_zero))
"""Validated type for a number (int or float) that is not zero.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `int` or `float`.
    2. Value must not be equal to 0 (negated `is_zero`).

Example:
    @validate_call
    def process(value: int_float_not_zero): ...
"""
