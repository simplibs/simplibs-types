from typing import Any
from typing import Annotated
from simplibs.rules import has_length


def tuple_min_length(min_length: int) -> Any:
    """Validated type for a tuple with a minimum number of items.

    Init Params:
        min_length (int): The minimum number of items the tuple must
            contain (inclusive).

    Validation pipeline:
        1. Value must be of type `tuple`.
        2. Value's length must be greater than or equal to `min_length`.

    Example:
        NonTrivialTuple = tuple_min_length(2)

        @validate_call
        def process(items: NonTrivialTuple): ...
    """
    return Annotated[tuple, has_length(min_length=min_length)]