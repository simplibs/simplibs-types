from typing import Annotated
from simplibs.rules import not_empty


bytes_not_empty = Annotated[bytes, not_empty]
"""Validated type for non-empty bytes.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `bytes`.
    2. Value must not be empty (length at least 1).

Example:
    @validate_call
    def process(value: bytes_not_empty): ...
"""