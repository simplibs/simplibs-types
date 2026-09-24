from simplibs.validate import validated_type
from simplibs.rules import is_blank


str_blank = validated_type(str, is_blank)
"""Validated type for a blank string (empty or whitespace-only).

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `str`.
    2. Value must be blank — empty or containing only whitespace characters.

Example:
    @validate_call
    def process(value: str_blank): ...
"""