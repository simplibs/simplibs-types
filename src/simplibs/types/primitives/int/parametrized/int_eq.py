from typing import Any
from simplibs.validate import validated_type
from simplibs.rules import equals


def int_eq(expected: int) -> Any:
    """Validated type for an integer equal to a specific expected value.

    Init Params:
        expected (int): The value the integer must equal.

    Validation pipeline:
        1. Value must be of type `int`.
        2. Value must equal `expected`.

    Example:
        MustBeSeven = int_eq(7)

        @validate_call
        def process(value: MustBeSeven): ...
    """
    return validated_type(int, equals(expected))