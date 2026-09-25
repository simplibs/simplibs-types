from typing import Any
from typing import Annotated
from simplibs.rules import has_length


def bytes_length_range(min_length: int, max_length: int) -> Any:
    """Validated type for bytes whose length falls within a given inclusive
    range.

    Init Params:
        min_length (int): The inclusive minimum length.
        max_length (int): The inclusive maximum length.

    Validation pipeline:
        1. Value must be of type `bytes`.
        2. Value's length must lie within the inclusive range
           [`min_length`, `max_length`].

    Example:
        TokenBytes = bytes_length_range(16, 32)

        @validate_call
        def process(value: TokenBytes): ...
    """
    return Annotated[bytes, has_length(min_length=min_length, max_length=max_length)]