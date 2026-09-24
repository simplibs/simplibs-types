from simplibs.validate import validated_type
from simplibs.rules import not_empty


tuple_not_empty = validated_type(tuple, not_empty)
"""Validated type for a non-empty tuple.

Init Params:
    (no parameters)

Validation pipeline:
    1. Value must be of type `tuple`.
    2. Value must not be empty (must contain at least one item).

Example:
    @validate_call
    def process(items: tuple_not_empty): ...
"""