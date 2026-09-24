# Direct:
from .direct.int_positive import int_positive
from .direct.int_negative import int_negative
from .direct.int_non_negative import int_non_negative
from .direct.int_non_positive import int_non_positive
from .direct.int_zero import int_zero
from .direct.int_not_zero import int_not_zero
from .direct.int_even import int_even
from .direct.int_odd import int_odd
from .direct.int_positive_even import int_positive_even
from .direct.int_positive_odd import int_positive_odd
from .direct.int_non_negative_even import int_non_negative_even
from .direct.int_uint8 import int_uint8
from .direct.int_int8 import int_int8
from .direct.int_percentage import int_percentage
from .direct.int_port import int_port
from .direct.int_year import int_year
from .direct.int_month import int_month
from .direct.int_day_of_month import int_day_of_month
from .direct.int_hour import int_hour
from .direct.int_minute import int_minute
from .direct.int_second import int_second
# Parametric:
from .parametrized.int_gt import int_gt
from .parametrized.int_ge import int_ge
from .parametrized.int_lt import int_lt
from .parametrized.int_le import int_le
from .parametrized.int_eq import int_eq
from .parametrized.int_ne import int_ne
from .parametrized.int_in_range import int_in_range
from .parametrized.int_divisible_by import int_divisible_by
from .parametrized.int_multiple_of import int_multiple_of


_DESIGN_NOTES = """
# Int Presets Sub-Package

## Purpose
Validated types for `int` — sign, zero, parity, combined sign+parity,
common bounded ranges (byte ranges, percentages, ports, calendar/time
fields), and parameterized comparisons, equality, and divisibility.

## Internal Components Registry

| Component                | Type            | Description                                         |
| :-------------------------- | :-------------- | :------------------------------------------------------ |
| `int_positive`              | Validated Type  | Positive integer.                                         |
| `int_negative`              | Validated Type  | Negative integer.                                         |
| `int_non_negative`          | Validated Type  | Non-negative integer.                                     |
| `int_non_positive`          | Validated Type  | Non-positive integer.                                     |
| `int_zero`                  | Validated Type  | Integer equal to zero.                                    |
| `int_not_zero`              | Validated Type  | Integer not equal to zero.                                |
| `int_even`                  | Validated Type  | Even integer.                                             |
| `int_odd`                   | Validated Type  | Odd integer.                                              |
| `int_positive_even`         | Validated Type  | Positive, even integer.                                   |
| `int_positive_odd`          | Validated Type  | Positive, odd integer.                                    |
| `int_non_negative_even`     | Validated Type  | Non-negative, even integer.                               |
| `int_uint8`                 | Validated Type  | Integer in unsigned 8-bit range [0, 255].                 |
| `int_int8`                  | Validated Type  | Integer in signed 8-bit range [-128, 127].                |
| `int_percentage`            | Validated Type  | Integer percentage [0, 100].                              |
| `int_port`                  | Validated Type  | Integer network port [0, 65535].                          |
| `int_year`                  | Validated Type  | Integer calendar year [1, 9999].                          |
| `int_month`                 | Validated Type  | Integer calendar month [1, 12].                           |
| `int_day_of_month`          | Validated Type  | Integer day of month [1, 31].                             |
| `int_hour`                  | Validated Type  | Integer hour, 24h clock [0, 23].                          |
| `int_minute`                | Validated Type  | Integer minute [0, 59].                                   |
| `int_second`                | Validated Type  | Integer second [0, 59].                                   |
| `int_gt`                    | Factory         | Integer strictly greater than a threshold.                |
| `int_ge`                    | Factory         | Integer greater than or equal to a threshold.             |
| `int_lt`                    | Factory         | Integer strictly less than a threshold.                   |
| `int_le`                    | Factory         | Integer less than or equal to a threshold.                |
| `int_eq`                    | Factory         | Integer equal to a specific value.                        |
| `int_ne`                    | Factory         | Integer not equal to a specific value.                    |
| `int_in_range`              | Factory         | Integer within an inclusive range.                        |
| `int_divisible_by`          | Factory         | Integer evenly divisible by a divisor.                    |
| `int_multiple_of`           | Factory         | Alias of `int_divisible_by`.                              |
"""