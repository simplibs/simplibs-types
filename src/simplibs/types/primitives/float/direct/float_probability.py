from simplibs.validate import validated_type
from simplibs.rules import in_range


float_probability = validated_type(float, in_range(0.0, 1.0))
"""Validated type for a float representing a probability.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `float`.
    2. Value must lie within the inclusive range [0.0, 1.0].

Example:
    @validate_call
    def process(value: float_probability): ...
"""