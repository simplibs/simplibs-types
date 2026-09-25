from typing import Any
from typing import Annotated
from simplibs.rules import for_each


def set_of(item_rule: Any) -> Any:
    """Validated type for a set whose every item satisfies a given rule.

    Init Params:
        item_rule (Rule | Callable[[Any], bool]): Rule that every single
            item of the set must satisfy.

    Validation pipeline:
        1. Value must be of type `set`.
        2. Every item of the set must satisfy `item_rule`.

    Detailed description:
        `item_rule` is applied to each item individually (see `for_each`) —
        if validation fails for a single item, validation of the whole
        set fails. `item_rule` itself may be an arbitrarily composed rule
        (e.g. via `&`, `|`, `~`), including another `validated_type` used
        as a nested annotation. Note that, unlike `list`/`tuple`, set
        items have no defined order.

    Example:
        PositiveIntSet = set_of(greater_than(0))

        @validate_call
        def register(scores: PositiveIntSet): ...
    """
    return Annotated[set, for_each(item_rule)]