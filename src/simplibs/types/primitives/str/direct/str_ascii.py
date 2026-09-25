from typing import Annotated
from simplibs.rules import is_ascii


str_ascii = Annotated[str, is_ascii]
"""Validated type for a string consisting entirely of ASCII characters.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `str`.
    2. Value must consist entirely of ASCII characters.

Example:
    @validate_call
    def process(value: str_ascii): ...
"""