from typing import Any
from simplibs.validate import validated_type
from simplibs.rules import contains


def str_contains(substring: str) -> Any:
    """Validated type for a string that must contain a given substring.

    Init Params:
        substring (str): The substring that must be present somewhere in
            the value.

    Validation pipeline:
        1. Value must be of type `str`.
        2. Value must contain `substring`.

    Example:
        MustMentionError = str_contains("error")

        @validate_call
        def process(value: MustMentionError): ...
    """
    return validated_type(str, contains(substring))