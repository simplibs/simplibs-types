from typing import Any
from simplibs.validate import validated_type
from simplibs.rules import has_length


def str_min_length(min_length: int) -> Any:
    """Validated type for a string with a minimum length.

    Init Params:
        min_length (int): The minimum number of characters the string
            must contain (inclusive).

    Validation pipeline:
        1. Value must be of type `str`.
        2. Value's length must be greater than or equal to `min_length`.

    Example:
        NonTrivialStr = str_min_length(3)

        @validate_call
        def process(value: NonTrivialStr): ...
    """
    return validated_type(str, has_length(min_length=min_length))