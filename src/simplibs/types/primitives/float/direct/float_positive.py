from simplibs.validate import validated_type
from simplibs.rules import greater_than


float_positive = validated_type(float, greater_than(0.0))
"""Validated type for a positive float (strictly greater than zero).

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `float`.
    2. Value must be strictly greater than 0.0.

Example:
    @validate_call
    def process(value: float_positive): ...
"""