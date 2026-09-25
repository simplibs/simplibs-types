from typing import Any
from typing import Annotated
from simplibs.rules import has_length


def tuple_max_length(max_length: int) -> Any:
    """Validated type for a tuple with a maximum number of items.

    Init Params:
        max_length (int): The maximum number of items the tuple may
            contain (inclusive).

    Validation pipeline:
        1. Value must be of type `tuple`.
        2. Value's length must be less than or equal to `max_length`.

    Example:
        SmallTuple = tuple_max_length(10)

        @validate_call
        def process(items: SmallTuple): ...
    """
    return Annotated[tuple, has_length(max_length=max_length)]