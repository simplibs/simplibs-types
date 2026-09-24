from typing import Any
from simplibs.validate import validated_type
from simplibs.rules import in_range


def float_in_range(min_val: float, max_val: float) -> Any:
    """Validated type for a float within a given inclusive range.

    Init Params:
        min_val (float): The inclusive lower bound.
        max_val (float): The inclusive upper bound.

    Validation pipeline:
        1. Value must be of type `float`.
        2. Value must lie within the inclusive range [`min_val`, `max_val`].

    Example:
        UnitRange = float_in_range(0.0, 1.0)

        @validate_call
        def process(value: UnitRange): ...
    """
    return validated_type(float, in_range(min_val, max_val))