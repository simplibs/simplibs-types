from simplibs.validate import validated_type
from simplibs.rules import in_range


int_minute = validated_type(int, in_range(0, 59))
"""Validated type for an integer representing a minute.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `int`.
    2. Value must lie within the inclusive range [0, 59].

Example:
    @validate_call
    def process(value: int_minute): ...
"""