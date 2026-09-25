from typing import Any
from typing import Annotated
from simplibs.rules import less_or_equal


def int_le(threshold: int) -> Any:
    """Validated type for an integer less than or equal to a given threshold.

    Init Params:
        threshold (int): The inclusive upper bound.

    Validation pipeline:
        1. Value must be of type `int`.
        2. Value must be less than or equal to `threshold`.

    Example:
        AtMostHundred = int_le(100)

        @validate_call
        def process(value: AtMostHundred): ...
    """
    return Annotated[int, less_or_equal(threshold)]