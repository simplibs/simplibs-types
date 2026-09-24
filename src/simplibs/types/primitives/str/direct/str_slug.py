from simplibs.validate import validated_type
from simplibs.rules import regex


str_slug = validated_type(str, regex(r"^[a-z0-9]+(?:-[a-z0-9]+)*$"))
"""Validated type for a URL-friendly slug string.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `str`.
    2. Value must fully match the pattern
       `^[a-z0-9]+(?:-[a-z0-9]+)*$` — lowercase letters and digits,
       grouped into hyphen-separated segments (e.g. `my-blog-post`).

Example:
    @validate_call
    def process(value: str_slug): ...
"""