# Direct:
from .direct.list_not_empty import list_not_empty
from .direct.list_unique import list_unique
from .direct.list_unique_not_empty import list_unique_not_empty
# Parametric:
from .parametrized.list_of import list_of
from .parametrized.list_length import list_length
from .parametrized.list_min_length import list_min_length
from .parametrized.list_max_length import list_max_length


_DESIGN_NOTES = """
# List Presets Sub-Package

## Purpose
Validated types for `list` — non-emptiness, item uniqueness, per-item
validation via `list_of`, and length constraints (exact, minimum, maximum).

## Internal Components Registry

| Component               | Type            | Description                                       |
| :----------------------- | :-------------- | :-------------------------------------------------- |
| `list_not_empty`         | Validated Type  | Non-empty list.                                      |
| `list_unique`            | Validated Type  | List with all unique items.                          |
| `list_unique_not_empty`  | Validated Type  | Non-empty list with all unique items.                |
| `list_of`                | Factory         | List whose every item satisfies a given rule.        |
| `list_length`            | Factory         | List with an exact number of items.                  |
| `list_min_length`        | Factory         | List with a minimum number of items.                 |
| `list_max_length`        | Factory         | List with a maximum number of items.                 |
"""