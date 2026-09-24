from typing import Any
from simplibs.validate import validated_type
from simplibs.rules import has_length


def bytes_max_length(max_length: int) -> Any:
    """Validated type for bytes with a maximum length.

    Init Params:
        max_length (int): The maximum number of bytes the value may
            contain (inclusive).

    Validation pipeline:
        1. Value must be of type `bytes`.
        2. Value's length must be less than or equal to `max_length`.

    Example:
        SmallBytes = bytes_max_length(1024)

        @validate_call
        def process(value: SmallBytes): ...
    """
    return validated_type(bytes, has_length(max_length=max_length))