from simplibs.validate import validated_type
from simplibs.rules import in_range


int_year = validated_type(int, in_range(1, 9999))
"""Validated type for an integer representing a calendar year.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `int`.
    2. Value must lie within the inclusive range [1, 9999].

Example:
    @validate_call
    def process(value: int_year): ...
"""