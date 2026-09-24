from simplibs.validate import validated_type
from simplibs.rules import less_than


float_negative = validated_type(float, less_than(0.0))
"""Validated type for a negative float (strictly less than zero).

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `float`.
    2. Value must be strictly less than 0.0.

Example:
    @validate_call
    def process(value: float_negative): ...
"""