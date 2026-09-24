from simplibs.validate import validated_type
from simplibs.rules import less_than


int_negative = validated_type(int, less_than(0))
"""Validated type for a negative integer (strictly less than zero).

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `int`.
    2. Value must be strictly less than 0.

Example:
    @validate_call
    def process(value: int_negative): ...
"""