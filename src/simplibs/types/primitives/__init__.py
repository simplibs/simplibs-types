# src/simplibs/03_simplibs-types/presets/types/__init__.py
_DESIGN_NOTES = """
# Scalar Types Presets Package

## Purpose
Validated types for Python's built-in scalar types. Each sub-package
groups one scalar type's presets (sign, zero, ranges, patterns, and
other type-specific constraints).

## Internal Components Registry

| Component  | Type      | Description                                              |
| :---------- | :-------- | :------------------------------------------------------------ |
| `bool`      | Sub-Package | Presets for `bool` (fixed truthy/falsy values).               |
| `bytes`     | Sub-Package | Presets for `bytes` (emptiness, length).                       |
| `float`     | Sub-Package | Presets for `float` (sign, zero, NaN/infinity, ranges).        |
| `int`       | Sub-Package | Presets for `int` (sign, zero, parity, ranges, divisibility).  |
| `number`    | Sub-Package | Presets for `int | float` (sign, zero, finiteness, ranges).    |
| `str`       | Sub-Package | Presets for `str` (emptiness, character classes, patterns).    |
"""