from simplibs.validate import validated_type
from simplibs.rules import is_titlecase


str_title = validated_type(str, is_titlecase)
"""Validated type for a string in title case.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `str`.
    2. Value must be in title case (each word capitalized).

Example:
    @validate_call
    def process(value: str_title): ...
"""