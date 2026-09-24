from simplibs.validate import validated_type
from simplibs.rules import is_digit_string


str_digit = validated_type(str, is_digit_string)
"""Validated type for a string consisting entirely of digit characters.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `str`.
    2. Value must consist entirely of digit characters.

Example:
    @validate_call
    def process(value: str_digit): ...
"""