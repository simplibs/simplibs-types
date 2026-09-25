from typing import Annotated
from simplibs.rules import is_true


bool_true = Annotated[bool, is_true]
"""Validated type for a boolean that must be True.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `bool`.
    2. Value must be `True`.

Example:
    @validate_call
    def process(flag: bool_true): ...
"""
