from typing import Any
from typing import Annotated
from simplibs.rules import has_length


def bytes_length(exact: int) -> Any:
    """Validated type for bytes with an exact length.

    Init Params:
        exact (int): The exact number of bytes the value must contain.

    Validation pipeline:
        1. Value must be of type `bytes`.
        2. Value's length must equal `exact`.

    Example:
        Md5Digest = bytes_length(16)

        @validate_call
        def process(value: Md5Digest): ...
    """
    return Annotated[bytes, has_length(exact)]