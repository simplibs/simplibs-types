from typing import Any
from typing import Annotated
from simplibs.rules import has_length


def str_max_length(max_length: int) -> Any:
    """Validated type for a string with a maximum length.

    Init Params:
        max_length (int): The maximum number of characters the string
            may contain (inclusive).

    Validation pipeline:
        1. Value must be of type `str`.
        2. Value's length must be less than or equal to `max_length`.

    Example:
        ShortStr = str_max_length(50)

        @validate_call
        def process(value: ShortStr): ...
    """
    return Annotated[str, has_length(max_length=max_length)]
