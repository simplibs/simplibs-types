from typing import Any
from simplibs.validate import validated_type
from simplibs.rules import has_length


def bytes_min_length(min_length: int) -> Any:
    """Validated type for bytes with a minimum length.

    Init Params:
        min_length (int): The minimum number of bytes the value must
            contain (inclusive).

    Validation pipeline:
        1. Value must be of type `bytes`.
        2. Value's length must be greater than or equal to `min_length`.

    Example:
        NonTrivialBytes = bytes_min_length(4)

        @validate_call
        def process(value: NonTrivialBytes): ...
    """
    return validated_type(bytes, has_length(min_length=min_length))