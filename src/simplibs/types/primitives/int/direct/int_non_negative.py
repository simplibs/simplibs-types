from simplibs.validate import validated_type
from simplibs.rules import greater_or_equal


int_non_negative = validated_type(int, greater_or_equal(0))
"""Validated type for a non-negative integer (zero or positive).

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `int`.
    2. Value must be greater than or equal to 0.

Example:
    @validate_call
    def process(value: int_non_negative): ...
"""