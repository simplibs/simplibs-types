from typing import Any
from typing import Annotated
from simplibs.rules import regex


def str_matches(pattern: str) -> Any:
    """Validated type for a string that must fully match a given regular
    expression pattern.

    Init Params:
        pattern (str): The regular expression the value must match.

    Validation pipeline:
        1. Value must be of type `str`.
        2. Value must match `pattern`.

    Example:
        DigitsOnly = str_matches(r"^\\d+$")

        @validate_call
        def process(value: DigitsOnly): ...
    """
    return Annotated[str, regex(pattern)]