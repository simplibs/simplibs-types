from typing import Any
from typing import Annotated
from simplibs.rules import has_length


def list_length(exact: int) -> Any:
    """Validated type for a list with an exact number of items.

    Init Params:
        exact (int): The exact number of items the list must contain.

    Validation pipeline:
        1. Value must be of type `list`.
        2. Value's length must equal `exact`.

    Example:
        TripletList = list_length(3)

        @validate_call
        def process(items: TripletList): ...
    """
    return Annotated[list, has_length(exact)]