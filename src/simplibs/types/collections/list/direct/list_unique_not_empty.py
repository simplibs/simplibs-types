from typing import Annotated
from simplibs.rules import not_empty, all_unique


list_unique_not_empty = Annotated[list, not_empty & all_unique]
"""Validated type for a non-empty list whose items are all unique.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `list`.
    2. Value must not be empty (must contain at least one item).
    3. All items in the list must be unique (no duplicates).

Example:
    @validate_call
    def process(items: list_unique_not_empty): ...
"""