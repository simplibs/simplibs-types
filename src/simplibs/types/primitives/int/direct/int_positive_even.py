from simplibs.validate import validated_type
from simplibs.rules import greater_than, is_even


int_positive_even = validated_type(int, greater_than(0) & is_even)
"""Validated type for a positive, even integer.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `int`.
    2. Value must be strictly greater than 0.
    3. Value must be even.

Example:
    @validate_call
    def process(value: int_positive_even): ...
"""