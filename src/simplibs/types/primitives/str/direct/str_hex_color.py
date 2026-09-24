from simplibs.validate import validated_type
from simplibs.rules import regex


str_hex_color = validated_type(str, regex(r"^#[0-9a-fA-F]{6}$"))
"""Validated type for a string in 6-digit hex color format.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `str`.
    2. Value must fully match the pattern `^#[0-9a-fA-F]{6}$` (a `#`
       followed by exactly 6 hexadecimal digits).

Example:
    @validate_call
    def process(value: str_hex_color): ...
"""