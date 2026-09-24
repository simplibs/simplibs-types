from simplibs.validate import validated_type
from simplibs.rules import regex


str_no_whitespace = validated_type(str, regex(r"^\S*$"))
"""Validated type for a string containing no whitespace characters at all.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `str`.
    2. Value must fully match the pattern `^\\S*$` (no whitespace
       characters anywhere in the string).

Example:
    @validate_call
    def process(value: str_no_whitespace): ...
"""