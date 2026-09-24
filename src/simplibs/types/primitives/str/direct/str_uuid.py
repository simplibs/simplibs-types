from simplibs.validate import validated_type
from simplibs.rules import regex


str_uuid = validated_type(str, regex(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"))
"""Validated type for a string in canonical UUID format.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `str`.
    2. Value must fully match the canonical UUID pattern
       (8-4-4-4-12 hexadecimal digit groups separated by hyphens).

Example:
    @validate_call
    def process(value: str_uuid): ...
"""