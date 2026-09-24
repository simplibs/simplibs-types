# src/simplibs/03_simplibs-types/presets/colections/__init__.py
_DESIGN_NOTES = """
# Collections Presets Package

## Purpose
Validated types for the four built-in container types. Each sub-package
groups one container's presets (non-emptiness, length constraints, item
uniqueness, per-item validation via `*_of` factories).

## Internal Components Registry

| Component  | Type      | Description                                       |
| :---------- | :-------- | :--------------------------------------------------- |
| `dict`      | Sub-Package | Presets for `dict` (emptiness, length).             |
| `list`      | Sub-Package | Presets for `list` (emptiness, uniqueness, length, `list_of`). |
| `set`       | Sub-Package | Presets for `set` (emptiness, length, `set_of`).     |
| `tuple`     | Sub-Package | Presets for `tuple` (emptiness, length, `tuple_of`). |
"""