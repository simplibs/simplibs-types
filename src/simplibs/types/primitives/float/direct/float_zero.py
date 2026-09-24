from simplibs.validate import validated_type
from simplibs.rules import is_zero


float_zero = validated_type(float, is_zero)
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