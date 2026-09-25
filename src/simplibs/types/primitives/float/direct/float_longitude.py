from typing import Annotated
from simplibs.rules import in_range


float_longitude = Annotated[float, in_range(-180.0, 180.0)]
"""Validated type for a float representing a geographic longitude.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `float`.
    2. Value must lie within the inclusive range [-180.0, 180.0].

Example:
    @validate_call
    def process(value: float_longitude): ...
"""