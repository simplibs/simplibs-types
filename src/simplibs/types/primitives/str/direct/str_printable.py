from typing import Annotated
from simplibs.rules import is_printable


str_printable = Annotated[str, is_printable]
"""Validated type for a string consisting entirely of printable
characters.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `str`.
    2. Value must consist entirely of printable characters (no control
       characters).

Example:
    @validate_call
    def process(value: str_printable): ...
"""