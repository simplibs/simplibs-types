from typing import Annotated
from simplibs.rules import not_empty


str_not_empty = Annotated[str, not_empty]
"""Validated type for a non-empty string.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `str`.
    2. Value must not be empty (length at least 1).

Detailed description:
    A non-empty string may still consist entirely of whitespace (e.g.
    `"   "`). Use `str_not_blank` if whitespace-only strings should also
    be rejected.

Example:
    @validate_call
    def process(value: str_not_empty): ...
"""