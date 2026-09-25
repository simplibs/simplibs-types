from typing import Annotated
from simplibs.rules import regex


str_snake_case = Annotated[str, regex(r"^[a-z][a-z0-9]*(?:_[a-z0-9]+)*$")]
"""Validated type for a snake_case string.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `str`.
    2. Value must fully match the pattern
       `^[a-z][a-z0-9]*(?:_[a-z0-9]+)*$` — starts with a lowercase
       letter, followed by lowercase alphanumeric segments separated by
       underscores (e.g. `my_variable_name`).

Example:
    @validate_call
    def process(value: str_snake_case): ...
"""