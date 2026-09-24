from typing import Any
from simplibs.validate import validated_type
from simplibs.rules import less_or_equal


def float_le(threshold: float) -> Any:
    """Validated type for a float less than or equal to a given threshold.

    Init Params:
        threshold (float): The inclusive upper bound.

    Validation pipeline:
        1. Value must be of type `float`.
        2. Value must be less than or equal to `threshold`.

    Example:
        AtMostHundred = float_le(100.0)

        @validate_call
        def process(value: AtMostHundred): ...
    """
    return validated_type(float, less_or_equal(threshold))