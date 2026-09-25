from typing import Annotated
from simplibs.rules import is_whitespace


str_whitespace = Annotated[str, is_whitespace]
"""Validated type for a string consisting entirely of whitespace
characters.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `str`.
    2. Value must consist entirely of whitespace characters (and be
       non-empty).

Example:
    @validate_call
    def process(value: str_whitespace): ...
"""