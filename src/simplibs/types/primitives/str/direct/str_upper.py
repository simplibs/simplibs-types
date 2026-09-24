from simplibs.validate import validated_type
from simplibs.rules import is_uppercase


str_upper = validated_type(str, is_uppercase)
"""Validated type for a string that is entirely uppercase.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `str`.
    2. Value must be entirely uppercase.

Example:
    @validate_call
    def process(value: str_upper): ...
"""