from simplibs.validate import validated_type
from simplibs.rules import is_lowercase


str_lower = validated_type(str, is_lowercase)
"""Validated type for a string that is entirely lowercase.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `str`.
    2. Value must be entirely lowercase.

Example:
    @validate_call
    def process(value: str_lower): ...
"""