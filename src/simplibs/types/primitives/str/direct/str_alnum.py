from typing import Annotated
from simplibs.rules import is_alnum


str_alnum = Annotated[str, is_alnum]
"""Validated type for a string consisting entirely of alphanumeric
characters.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `str`.
    2. Value must consist entirely of alphanumeric characters (letters
       and/or digits).

Example:
    @validate_call
    def process(value: str_alnum): ...
"""