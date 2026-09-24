from simplibs.validate import validated_type
from simplibs.rules import less_or_equal


int_float_non_positive = validated_type(int | float, less_or_equal(0))
"""Validated type for a non-positive number (int or float, zero or
negative).

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `int` or `float`.
    2. Value must be less than or equal to 0.

Example:
    @validate_call
    def process(value: int_float_non_positive): ...
"""