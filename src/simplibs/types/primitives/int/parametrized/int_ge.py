from typing import Any
from typing import Annotated
from simplibs.rules import greater_or_equal


def int_ge(threshold: int) -> Any:
    """Validated type for an integer greater than or equal to a given
    threshold.

    Init Params:
        threshold (int): The inclusive lower bound.

    Validation pipeline:
        1. Value must be of type `int`.
        2. Value must be greater than or equal to `threshold`.

    Example:
        AtLeastZero = int_ge(0)

        @validate_call
        def process(value: AtLeastZero): ...
    """
    return Annotated[int, greater_or_equal(threshold)]