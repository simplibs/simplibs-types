from typing import Any
from simplibs.validate import validated_type
from simplibs.rules import ends_with


def str_ends_with(suffix: str) -> Any:
    """Validated type for a string that must end with a given suffix.

    Init Params:
        suffix (str): The required suffix.

    Validation pipeline:
        1. Value must be of type `str`.
        2. Value must end with `suffix`.

    Example:
        PdfFilename = str_ends_with(".pdf")

        @validate_call
        def process(value: PdfFilename): ...
    """
    return validated_type(str, ends_with(suffix))