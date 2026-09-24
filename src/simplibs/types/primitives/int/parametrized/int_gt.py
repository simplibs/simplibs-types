from typing import Any
from simplibs.validate import validated_type
from simplibs.rules import greater_than


def int_gt(threshold: int) -> Any:
    """Validated type for an integer strictly greater than a given threshold.

    Init Params:
        threshold (int): The exclusive lower bound.

    Validation pipeline:
        1. Value must be of type `int`.
        2. Value must be strictly greater than `threshold`.

    Example:
        AboveZero = int_gt(0)

        @validate_call
        def process(value: AboveZero): ...
    """
    return validated_type(int, greater_than(threshold))