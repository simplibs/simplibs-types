# Direct:
from .direct.tuple_not_empty import tuple_not_empty
# Parametric:
from .parametrized.tuple_of import tuple_of
from .parametrized.tuple_length import tuple_length
from .parametrized.tuple_min_length import tuple_min_length
from .parametrized.tuple_max_length import tuple_max_length


_DESIGN_NOTES = """
# Tuple Presets Sub-Package

## Purpose
Validated types for `tuple` — non-emptiness, per-item validation via
`tuple_of`, and length constraints (exact, minimum, maximum).

## Internal Components Registry

| Component            | Type            | Description                                    |
| :-------------------- | :-------------- | :----------------------------------------------- |
| `tuple_not_empty`     | Validated Type  | Non-empty tuple.                                  |
| `tuple_of`            | Factory         | Tuple whose every item satisfies a given rule.    |
| `tuple_length`        | Factory         | Tuple with an exact number of items.              |
| `tuple_min_length`    | Factory         | Tuple with a minimum number of items.             |
| `tuple_max_length`    | Factory         | Tuple with a maximum number of items.             |
"""