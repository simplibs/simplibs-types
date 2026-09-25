from typing import Any
from typing import Annotated
from simplibs.rules import less_than


def float_lt(threshold: float) -> Any:
    """Validated type for a float strictly less than a given threshold.

    Init Params:
        threshold (float): The exclusive upper bound.

    Validation pipeline:
        1. Value must be of type `float`.
        2. Value must be strictly less than `threshold`.

    Example:
        BelowHundred = float_lt(100.0)

        @validate_call
        def process(value: BelowHundred): ...
    """
    return Annotated[float, less_than(threshold)]