from typing import Annotated
from simplibs.rules import not_empty


set_not_empty = Annotated[set, not_empty]
"""Validated type for a non-empty set.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `set`.
    2. Value must not be empty (must contain at least one item).

Example:
    @validate_call
    def process(items: set_not_empty): ...
"""