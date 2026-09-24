from simplibs.validate import validated_type
from simplibs.rules import regex


str_url = validated_type(str, regex(r"^https?://[^\s]+$"))
"""Validated type for a string matching a basic HTTP(S) URL shape.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `str`.
    2. Value must fully match the pattern `^https?://[^\\s]+$`.

Detailed description:
    This only checks for an `http://` or `https://` prefix followed by
    non-whitespace characters — it does not validate the URL's structure
    beyond that (e.g. malformed hosts or paths may still pass).

Example:
    @validate_call
    def process(value: str_url): ...
"""