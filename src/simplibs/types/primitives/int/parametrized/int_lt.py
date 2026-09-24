from typing import Any
from simplibs.validate import validated_type
from simplibs.rules import less_than


def int_lt(threshold: int) -> Any:
    """Validated type for an integer strictly less than a given threshold.

    Init Params:
        threshold (int): The exclusive upper bound.

    Validation pipeline:
        1. Value must be of type `int`.
        2. Value must be strictly less than `threshold`.

    Example:
        BelowHundred = int_lt(100)

        @validate_call
        def process(value: BelowHundred): ...
    """
    return validated_type(int, less_than(threshold))