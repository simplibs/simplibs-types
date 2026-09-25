from typing import Any
from typing import Annotated
from simplibs.rules import in_range


def int_in_range(min_val: int, max_val: int) -> Any:
    """Validated type for an integer within a given inclusive range.

    Init Params:
        min_val (int): The inclusive lower bound.
        max_val (int): The inclusive upper bound.

    Validation pipeline:
        1. Value must be of type `int`.
        2. Value must lie within the inclusive range [`min_val`, `max_val`].

    Example:
        ScoreRange = int_in_range(0, 100)

        @validate_call
        def process(value: ScoreRange): ...
    """
    return Annotated[int, in_range(min_val, max_val)]