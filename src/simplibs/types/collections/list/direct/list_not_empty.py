from typing import Annotated
from simplibs.rules import not_empty


list_not_empty = Annotated[list, not_empty]
"""Validated type for a non-empty list.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `list`.
    2. Value must not be empty (must contain at least one item).

Example:
    @validate_call
    def process(items: list_not_empty): ...
"""