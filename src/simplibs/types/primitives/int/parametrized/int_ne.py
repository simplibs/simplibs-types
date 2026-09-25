from typing import Any
from typing import Annotated
from simplibs.rules import not_equals


def int_ne(forbidden: int) -> Any:
    """Validated type for an integer that must not equal a specific value.

    Init Params:
        forbidden (int): The value the integer must not equal.

    Validation pipeline:
        1. Value must be of type `int`.
        2. Value must not equal `forbidden`.

    Example:
        NotThirteen = int_ne(13)

        @validate_call
        def process(value: NotThirteen): ...
    """
    return Annotated[int, not_equals(forbidden)]