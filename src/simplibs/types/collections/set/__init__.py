# Direct:
from .direct.set_not_empty import set_not_empty
# Parametric:
from .parametrized.set_of import set_of
from .parametrized.set_length import set_length
from .parametrized.set_min_length import set_min_length
from .parametrized.set_max_length import set_max_length


_DESIGN_NOTES = """
# Set Presets Sub-Package

## Purpose
Validated types for `set` — non-emptiness, per-item validation via
`set_of`, and length constraints (exact, minimum, maximum).

## Internal Components Registry

| Component         | Type            | Description                                    |
| :----------------- | :-------------- | :----------------------------------------------- |
| `set_not_empty`    | Validated Type  | Non-empty set.                                    |
| `set_of`           | Factory         | Set whose every item satisfies a given rule.      |
| `set_length`       | Factory         | Set with an exact number of items.                |
| `set_min_length`   | Factory         | Set with a minimum number of items.               |
| `set_max_length`   | Factory         | Set with a maximum number of items.               |
"""