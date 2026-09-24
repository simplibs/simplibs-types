from typing import Any
# Inners
from .int_divisible_by import int_divisible_by


def int_multiple_of(divisor: int) -> Any:
    """Alias of `int_divisible_by` — validated type for an integer that is
    a multiple of a given divisor.

    Init Params:
        divisor (int): The number the value must be a multiple of.

    Validation pipeline:
        1. Value must be of type `int`.
        2. Value must be evenly divisible by `divisor` (no remainder).

    Detailed description:
        Provided as a more naturally-worded alias — "multiple of" reads
        better at call sites than "divisible by" in some contexts, but the
        underlying rule is identical. See `int_divisible_by` for the
        canonical implementation.

    Example:
        MultipleOfFive = int_multiple_of(5)

        @validate_call
        def process(value: MultipleOfFive): ...
    """
    return int_divisible_by(divisor)