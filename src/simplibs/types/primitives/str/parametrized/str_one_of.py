from typing import Any
from typing import Annotated
from simplibs.rules import is_in


def str_one_of(*options: str) -> Any:
    """Validated type for a string restricted to a fixed set of allowed
    values.

    Init Params:
        *options (str): The set of values the string is allowed to equal.

    Validation pipeline:
        1. Value must be of type `str`.
        2. Value must equal one of `options`.

    Example:
        Status = str_one_of("pending", "active", "closed")

        @validate_call
        def process(value: Status): ...
    """
    return Annotated[str, is_in(options)]