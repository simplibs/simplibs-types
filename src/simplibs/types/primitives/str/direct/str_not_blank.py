from typing import Annotated
from simplibs.rules import not_blank


str_not_blank = Annotated[str, not_blank]
"""Validated type for a string that is neither empty nor whitespace-only.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `str`.
    2. Value must not be blank (must contain at least one non-whitespace
       character).

Example:
    @validate_call
    def process(value: str_not_blank): ...
"""