from simplibs.validate import validated_type
from simplibs.rules import less_or_equal


float_non_positive = validated_type(float, less_or_equal(0.0))
"""Validated type for a non-positive float (zero or negative).

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `float`.
    2. Value must be less than or equal to 0.0.

Example:
    @validate_call
    def process(value: float_non_positive): ...
"""