from typing import Any
from simplibs.validate import validated_type
from simplibs.rules import has_length


def str_length(exact: int) -> Any:
    """Validated type for a string with an exact length.

    Init Params:
        exact (int): The exact number of characters the string must
            contain.

    Validation pipeline:
        1. Value must be of type `str`.
        2. Value's length must equal `exact`.

    Example:
        FourChars = str_length(4)

        @validate_call
        def process(value: FourChars): ...
    """
    return validated_type(str, has_length(exact))