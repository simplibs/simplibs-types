from simplibs.validate import validated_type
from simplibs.rules import is_empty


str_empty = validated_type(str, is_empty)
"""Validated type for an empty string.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `str`.
    2. Value must be empty (length 0).

Example:
    @validate_call
    def process(value: str_empty): ...
"""