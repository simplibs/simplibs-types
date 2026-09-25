from typing import Any
from typing import Annotated
from simplibs.rules import has_length


def str_length_range(min_length: int, max_length: int) -> Any:
    """Validated type for a string whose length falls within a given
    inclusive range.

    Init Params:
        min_length (int): The inclusive minimum length.
        max_length (int): The inclusive maximum length.

    Validation pipeline:
        1. Value must be of type `str`.
        2. Value's length must lie within the inclusive range
           [`min_length`, `max_length`].

    Example:
        UsernameStr = str_length_range(3, 20)

        @validate_call
        def process(value: UsernameStr): ...
    """
    return Annotated[str, has_length(min_length=min_length, max_length=max_length)]