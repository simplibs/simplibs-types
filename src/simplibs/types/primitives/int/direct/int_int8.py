from simplibs.validate import validated_type
from simplibs.rules import in_range


int_int8 = validated_type(int, in_range(-128, 127))
"""Validated type for an integer in the signed 8-bit range.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `int`.
    2. Value must lie within the inclusive range [-128, 127].

Example:
    @validate_call
    def process(value: int_int8): ...
"""