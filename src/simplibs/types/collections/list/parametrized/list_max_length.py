from typing import Any
from simplibs.validate import validated_type
from simplibs.rules import has_length


def list_max_length(max_length: int) -> Any:
    """Validated type for a list with a maximum number of items.

    Init Params:
        max_length (int): The maximum number of items the list may
            contain (inclusive).

    Validation pipeline:
        1. Value must be of type `list`.
        2. Value's length must be less than or equal to `max_length`.

    Example:
        SmallList = list_max_length(10)

        @validate_call
        def process(items: SmallList): ...
    """
    return validated_type(list, has_length(max_length=max_length))