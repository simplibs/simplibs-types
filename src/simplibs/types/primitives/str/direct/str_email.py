from typing import Annotated
from simplibs.rules import regex


str_email = Annotated[str, regex(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")]
"""Validated type for a string matching a basic email address shape.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `str`.
    2. Value must fully match the pattern `^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$`.

Detailed description:
    This is a lightweight structural check (local-part @ domain . tld),
    not a full RFC 5322 email validator — it accepts many strings that
    aren't real, deliverable addresses and is meant to catch obviously
    malformed input rather than guarantee validity.

Example:
    @validate_call
    def process(value: str_email): ...
"""