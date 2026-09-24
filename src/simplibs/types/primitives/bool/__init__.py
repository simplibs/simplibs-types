# Direct:
from .direct.bool_true import bool_true
from .direct.bool_false import bool_false


_DESIGN_NOTES = """
# Bool Presets Sub-Package

## Purpose
Validated types for `bool` — fixed truthy/falsy values.

## Internal Components Registry

| Component     | Type            | Description                     |
| :------------- | :-------------- | :-------------------------------- |
| `bool_true`    | Validated Type  | Boolean that must be `True`.      |
| `bool_false`   | Validated Type  | Boolean that must be `False`.     |
"""