from typing import Any
from typing import Annotated
from simplibs.rules import for_each


def list_of(item_rule: Any) -> Any:
    """Validated type for a list whose every item satisfies a given rule.

    Init Params:
        item_rule (Rule | Callable[[Any], bool]): Rule that every single
            item of the list must satisfy.

    Validation pipeline:
        1. Value must be of type `list`.
        2. Every item of the list must satisfy `item_rule`.

    Detailed description:
        `item_rule` is applied to each item individually (see `for_each`) —
        if validation fails for a single item, validation of the whole
        list fails. `item_rule` itself may be an arbitrarily composed rule
        (e.g. via `&`, `|`, `~`), including another `validated_type` used
        as a nested annotation.

    Example:
        PositiveIntList = list_of(greater_than(0))

        @validate_call
        def register(scores: PositiveIntList): ...
    """
    return Annotated[list, for_each(item_rule)]