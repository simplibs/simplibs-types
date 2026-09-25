from typing import Any
from typing import Annotated
from simplibs.rules import greater_than


def float_gt(threshold: float) -> Any:
    """Validated type for a float strictly greater than a given threshold.

    Init Params:
        threshold (float): The exclusive lower bound.

    Validation pipeline:
        1. Value must be of type `float`.
        2. Value must be strictly greater than `threshold`.

    Example:
        AboveZero = float_gt(0.0)

        @validate_call
        def process(value: AboveZero): ...
    """
    return Annotated[float, greater_than(threshold)]