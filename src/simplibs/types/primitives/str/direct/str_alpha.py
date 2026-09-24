from simplibs.validate import validated_type
from simplibs.rules import is_alpha


str_alpha = validated_type(str, is_alpha)
"""Validated type for a string consisting entirely of alphabetic
characters.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `str`.
    2. Value must consist entirely of alphabetic characters.

Example:
    @validate_call
    def process(value: str_alpha): ...
"""
