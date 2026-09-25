from typing import Annotated
from simplibs.rules import is_empty


bytes_empty = Annotated[bytes, is_empty]
"""Validated type for empty bytes.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `bytes`.
    2. Value must be empty (length 0).

Example:
    @validate_call
    def process(value: bytes_empty): ...
"""