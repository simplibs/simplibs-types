from simplibs.validate import validated_type
from simplibs.rules import in_range


int_hour = validated_type(int, in_range(0, 23))
"""Validated type for an integer representing an hour (24-hour clock).

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `int`.
    2. Value must lie within the inclusive range [0, 23].

Example:
    @validate_call
    def process(value: int_hour): ...
"""