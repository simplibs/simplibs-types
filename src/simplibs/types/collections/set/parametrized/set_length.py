from typing import Any
from typing import Annotated
from simplibs.rules import has_length


def set_length(exact: int) -> Any:
    """Validated type for a set with an exact number of items.

    Init Params:
        exact (int): The exact number of items the set must contain.

    Validation pipeline:
        1. Value must be of type `set`.
        2. Value's length must equal `exact`.

    Example:
        TripletSet = set_length(3)

        @validate_call
        def process(items: TripletSet): ...
    """
    return Annotated[set, has_length(exact)]