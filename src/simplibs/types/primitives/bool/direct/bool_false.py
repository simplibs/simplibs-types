from typing import Annotated
from simplibs.rules import is_false


bool_false = Annotated[bool, is_false]
"""Validated type for a boolean that must be False.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `bool`.
    2. Value must be `False`.

Example:
    @validate_call
    def process(flag: bool_false): ...
"""