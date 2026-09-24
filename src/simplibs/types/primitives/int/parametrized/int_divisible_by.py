from typing import Any
from simplibs.validate import validated_type
from simplibs.rules import divisible_by


def int_divisible_by(divisor: int) -> Any:
    """Validated type for an integer evenly divisible by a given divisor.

    Init Params:
        divisor (int): The number the value must be evenly divisible by.

    Validation pipeline:
        1. Value must be of type `int`.
        2. Value must be evenly divisible by `divisor` (no remainder).

    Example:
        MultipleOfFive = int_divisible_by(5)

        @validate_call
        def process(value: MultipleOfFive): ...
    """
    return validated_type(int, divisible_by(divisor))