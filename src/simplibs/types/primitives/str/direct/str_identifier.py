from typing import Annotated
from simplibs.rules import is_identifier


str_identifier = Annotated[str, is_identifier]
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