from typing import Any
from simplibs.validate import validated_type
from simplibs.rules import in_range

def int_float_in_range(min_val: Any, max_val: Any) -> Any:
    """Validated type for a number (int or float) within a given inclusive
    range.

    Init Params:
        min_val (Any): The inclusive lower bound.
        max_val (Any): The inclusive upper bound.

    Validation pipeline:
        1. Value must be of type `int` or `float`.
        2. Value must lie within the inclusive range [`min_val`, `max_val`].

    Example:
        ScoreRange = int_float_in_range(0, 100)

        @validate_call
        def process(value: ScoreRange): ...
    """
    return validated_type(int | float, in_range(min_val, max_val))