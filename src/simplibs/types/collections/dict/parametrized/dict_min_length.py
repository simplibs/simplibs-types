from typing import Any
from simplibs.validate import validated_type
from simplibs.rules import has_length


def dict_min_length(min_length: int) -> Any:
    """Validated type for a dictionary with a minimum number of items.

    Init Params:
        min_length (int): The minimum number of key-value pairs the
            dictionary must contain (inclusive).

    Validation pipeline:
        1. Value must be of type `dict`.
        2. Value's length must be greater than or equal to `min_length`.

    Example:
        NonTrivialDict = dict_min_length(2)

        @validate_call
        def process(data: NonTrivialDict): ...
    """
    return validated_type(dict, has_length(min_length=min_length))