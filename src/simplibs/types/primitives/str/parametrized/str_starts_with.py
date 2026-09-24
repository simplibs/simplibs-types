from typing import Any
from simplibs.validate import validated_type
from simplibs.rules import starts_with


def str_starts_with(prefix: str) -> Any:
    """Validated type for a string that must start with a given prefix.

    Init Params:
        prefix (str): The required prefix.

    Validation pipeline:
        1. Value must be of type `str`.
        2. Value must start with `prefix`.

    Example:
        HttpsUrl = str_starts_with("https://")

        @validate_call
        def process(value: HttpsUrl): ...
    """
    return validated_type(str, starts_with(prefix))
