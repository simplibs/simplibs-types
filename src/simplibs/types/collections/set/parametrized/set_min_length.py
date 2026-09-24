from typing import Any
from simplibs.validate import validated_type
from simplibs.rules import has_length


def set_min_length(min_length: int) -> Any:
    """Validated type for a set with a minimum number of items.

    Init Params:
        min_length (int): The minimum number of items the set must
            contain (inclusive).

    Validation pipeline:
        1. Value must be of type `set`.
        2. Value's length must be greater than or equal to `min_length`.

    Example:
        NonTrivialSet = set_min_length(2)

        @validate_call
        def process(items: NonTrivialSet): ...
    """
    return validated_type(set, has_length(min_length=min_length))