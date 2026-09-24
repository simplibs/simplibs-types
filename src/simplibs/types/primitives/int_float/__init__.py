# Direct:
from .direct.int_float_positive import int_float_positive
from .direct.int_float_negative import int_float_negative
from .direct.int_float_non_negative import int_float_non_negative
from .direct.int_float_non_positive import int_float_non_positive
from .direct.int_float_zero import int_float_zero
from .direct.int_float_not_zero import int_float_not_zero
from .direct.int_float_finite import int_float_finite
# Parametric:
from .parametrized.int_float_in_range import int_float_in_range


_DESIGN_NOTES = """
# Number Presets Sub-Package

## Purpose
Validated types for the `int | float` union (`Number`) — sign, zero,
finiteness, and generic ranges shared by both numeric types.

## Internal Components Registry

| Component                | Type            | Description                                    |
| :-------------------------- | :-------------- | :------------------------------------------------- |
| `int_float_positive`           | Validated Type  | Positive number (int or float).                     |
| `int_float_negative`           | Validated Type  | Negative number (int or float).                     |
| `int_float_non_negative`       | Validated Type  | Non-negative number (int or float).                 |
| `int_float_non_positive`       | Validated Type  | Non-positive number (int or float).                 |
| `int_float_zero`               | Validated Type  | Number equal to zero (int or float).                |
| `int_float_not_zero`           | Validated Type  | Number not equal to zero (int or float).            |
| `int_float_finite`             | Validated Type  | Finite number (int or float).                       |
| `int_float_in_range`           | Factory         | Number within an inclusive range (int or float).    |
"""