from typing import Annotated
from simplibs.rules import regex


str_single_line = Annotated[str, regex(r"^[^\n\r]*$")]
"""Validated type for a single-line string (no line breaks).

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `str`.
    2. Value must fully match the pattern `^[^\\n\\r]*$` (no newline or
       carriage return characters).

Example:
    @validate_call
    def process(value: str_single_line): ...
"""