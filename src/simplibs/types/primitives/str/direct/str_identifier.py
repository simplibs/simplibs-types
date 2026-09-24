from simplibs.validate import validated_type
from simplibs.rules import is_identifier


str_identifier = validated_type(str, is_identifier)
"""Validated type for a string that is a valid Python identifier.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `str`.
    2. Value must be a valid Python identifier (as per `str.isidentifier`).

Example:
    @validate_call
    def process(value: str_identifier): ...
"""