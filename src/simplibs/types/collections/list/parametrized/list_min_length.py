from typing import Any
from simplibs.validate import validated_type
from simplibs.rules import has_length


def list_min_length(min_length: int) -> Any:
    """Validated type for a list with a minimum number of items.

    Init Params:
        min_length (int): The minimum number of items the list must
            contain (inclusive).

    Validation pipeline:
        1. Value must be of type `list`.
        2. Value's length must be greater than or equal to `min_length`.

    Example:
        NonTrivialList = list_min_length(2)

        @validate_call
        def process(items: NonTrivialList): ...
    """
    return validated_type(list, has_length(min_length=min_length))