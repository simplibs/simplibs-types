from typing import Annotated
from simplibs.rules import in_range


int_port = Annotated[int, in_range(0, 65535)]
"""Validated type for an integer representing a network port number.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `int`.
    2. Value must lie within the inclusive range [0, 65535].

Example:
    @validate_call
    def process(value: int_port): ...
"""