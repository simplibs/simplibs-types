from typing import Annotated
from simplibs.rules import in_range


int_second = Annotated[int, in_range(0, 59)]
"""Validated type for an integer representing a second.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `int`.
    2. Value must lie within the inclusive range [0, 59].

Detailed description:
    This does not account for leap seconds (value 60) — only the
    standard [0, 59] range is accepted.

Example:
    @validate_call
    def process(value: int_second): ...
"""