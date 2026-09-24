from simplibs.validate import validated_type
from simplibs.rules import in_range


float_latitude = validated_type(float, in_range(-90.0, 90.0))
"""Validated type for a float representing a geographic latitude.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `float`.
    2. Value must lie within the inclusive range [-90.0, 90.0].

Example:
    @validate_call
    def process(value: float_latitude): ...
"""