from typing import Annotated
from simplibs.rules import all_unique


list_unique = Annotated[list, all_unique]
"""Validated type for a list whose items are all unique.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `list`.
    2. All items in the list must be unique (no duplicates).

Example:
    @validate_call
    def process(items: list_unique): ...
"""