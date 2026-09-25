from typing import Any, Annotated, Callable
from typing import Annotated
from simplibs.rules import has_length


def tuple_length(exact: int) -> Any:
    """Validated type for a tuple with an exact number of items.

    Init Params:
        exact (int): The exact number of items the tuple must contain.

    Validation pipeline:
        1. Value must be of type `tuple`.
        2. Value's length must equal `exact`.

    Example:
        TripletTuple = tuple_length(3)

        @validate_call
        def process(items: TripletTuple): ...
    """
    return Annotated[tuple, has_length(exact)]