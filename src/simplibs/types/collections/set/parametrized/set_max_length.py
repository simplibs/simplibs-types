from typing import Any
from simplibs.validate import validated_type
from simplibs.rules import has_length


def set_max_length(max_length: int) -> Any:
    """Validated type for a set with a maximum number of items.

    Init Params:
        max_length (int): The maximum number of items the set may
            contain (inclusive).

    Validation pipeline:
        1. Value must be of type `set`.
        2. Value's length must be less than or equal to `max_length`.

    Example:
        SmallSet = set_max_length(10)

        @validate_call
        def process(items: SmallSet): ...
    """
    return validated_type(set, has_length(max_length=max_length))