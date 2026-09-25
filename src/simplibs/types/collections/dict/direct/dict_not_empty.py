from typing import Annotated
from simplibs.rules import not_empty


dict_not_empty = Annotated[dict, not_empty]
"""Validated type for a non-empty dictionary.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `dict`.
    2. Value must not be empty (must contain at least one item).

Example:
    @validate_call
    def process(data: dict_not_empty): ...
"""