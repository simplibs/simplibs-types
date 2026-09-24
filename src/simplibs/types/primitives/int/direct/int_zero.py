from simplibs.validate import validated_type
from simplibs.rules import is_zero


int_zero = validated_type(int, is_zero)
"""Validated type for an integer equal to zero.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `int`.
    2. Value must be equal to 0.

Example:
    @validate_call
    def process(value: int_zero): ...
"""