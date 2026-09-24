from typing import Any
from simplibs.validate import validated_type
from simplibs.rules import has_length


def dict_length(exact: int) -> Any:
    """Validated type for a dictionary with an exact number of items.

    Init Params:
        exact (int): The exact number of key-value pairs the dictionary
            must contain.

    Validation pipeline:
        1. Value must be of type `dict`.
        2. Value's length must equal `exact`.

    Example:
        ThreeItemDict = dict_length(3)

        @validate_call
        def process(data: ThreeItemDict): ...
    """
    return validated_type(dict, has_length(exact))