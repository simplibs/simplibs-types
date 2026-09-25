from typing import Any
from typing import Annotated
from simplibs.rules import has_length


def dict_max_length(max_length: int) -> Any:
    """Validated type for a dictionary with a maximum number of items.

    Init Params:
        max_length (int): The maximum number of key-value pairs the
            dictionary may contain (inclusive).

    Validation pipeline:
        1. Value must be of type `dict`.
        2. Value's length must be less than or equal to `max_length`.

    Example:
        SmallDict = dict_max_length(10)

        @validate_call
        def process(data: SmallDict): ...
    """
    return Annotated[dict, has_length(max_length=max_length)]