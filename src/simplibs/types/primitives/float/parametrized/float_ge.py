from typing import Any
from simplibs.validate import validated_type
from simplibs.rules import greater_or_equal


def float_ge(threshold: float) -> Any:
    """Validated type for a float greater than or equal to a given threshold.

    Init Params:
        threshold (float): The inclusive lower bound.

    Validation pipeline:
        1. Value must be of type `float`.
        2. Value must be greater than or equal to `threshold`.

    Example:
        AtLeastZero = float_ge(0.0)

        @validate_call
        def process(value: AtLeastZero): ...
    """
    return validated_type(float, greater_or_equal(threshold))