from typing import Any
from simplibs.validate import validated_type
from simplibs.rules import for_each


def tuple_of(item_rule: Any) -> Any:
    """Validated type for a tuple whose every item satisfies a given rule.

    Init Params:
        item_rule (Rule | Callable[[Any], bool]): Rule that every single
            item of the tuple must satisfy.

    Validation pipeline:
        1. Value must be of type `tuple`.
        2. Every item of the tuple must satisfy `item_rule`.

    Detailed description:
        `item_rule` is applied to each item individually (see `for_each`) —
        if validation fails for a single item, validation of the whole
        tuple fails. `item_rule` itself may be an arbitrarily composed rule
        (e.g. via `&`, `|`, `~`), including another `validated_type` used
        as a nested annotation. This applies `item_rule` uniformly to
        every position; it does not validate fixed-position tuples of
        mixed types (e.g. `tuple[int, str]`) element-by-element.

    Example:
        PositiveIntTuple = tuple_of(greater_than(0))

        @validate_call
        def register(scores: PositiveIntTuple): ...
    """
    return validated_type(tuple, for_each(item_rule))