# Direct:
from .direct.dict_not_empty import dict_not_empty
# Parametric:
from .parametrized.dict_length import dict_length
from .parametrized.dict_min_length import dict_min_length
from .parametrized.dict_max_length import dict_max_length


_DESIGN_NOTES = """
# Dict Presets Sub-Package

## Purpose
Validated types for `dict` — non-emptiness and length constraints (exact,
minimum, maximum number of key-value pairs).

## Internal Components Registry

| Component          | Type            | Description                                    |
| :------------------ | :-------------- | :---------------------------------------------- |
| `dict_not_empty`    | Validated Type  | Non-empty dictionary.                            |
| `dict_length`       | Factory         | Dictionary with an exact number of items.        |
| `dict_min_length`   | Factory         | Dictionary with a minimum number of items.       |
| `dict_max_length`   | Factory         | Dictionary with a maximum number of items.       |
"""