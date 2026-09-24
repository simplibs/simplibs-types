# Direct:
from .direct.float_positive import float_positive
from .direct.float_negative import float_negative
from .direct.float_non_negative import float_non_negative
from .direct.float_non_positive import float_non_positive
from .direct.float_zero import float_zero
from .direct.float_not_zero import float_not_zero
from .direct.float_finite import float_finite
from .direct.float_not_nan import float_not_nan
from .direct.float_not_infinite import float_not_infinite
from .direct.float_probability import float_probability
from .direct.float_percentage import float_percentage
from .direct.float_latitude import float_latitude
from .direct.float_longitude import float_longitude
# Parametric:
from .parametrized.float_gt import float_gt
from .parametrized.float_ge import float_ge
from .parametrized.float_lt import float_lt
from .parametrized.float_le import float_le
from .parametrized.float_in_range import float_in_range


_DESIGN_NOTES = """
# Float Presets Sub-Package

## Purpose
Validated types for `float` — sign, zero, special IEEE-754 states (NaN,
infinity), common bounded ranges (probability, percentage, latitude,
longitude), and parameterized comparisons.

## Internal Components Registry

| Component               | Type            | Description                                        |
| :------------------------ | :-------------- | :----------------------------------------------------- |
| `float_positive`          | Validated Type  | Positive float.                                          |
| `float_negative`          | Validated Type  | Negative float.                                          |
| `float_non_negative`      | Validated Type  | Non-negative float.                                      |
| `float_non_positive`      | Validated Type  | Non-positive float.                                      |
| `float_zero`              | Validated Type  | Float equal to zero.                                     |
| `float_not_zero`          | Validated Type  | Float not equal to zero.                                 |
| `float_finite`            | Validated Type  | Finite float (not NaN, not infinite).                    |
| `float_not_nan`           | Validated Type  | Float that is not NaN.                                   |
| `float_not_infinite`      | Validated Type  | Float that is not +/-infinity.                           |
| `float_probability`       | Validated Type  | Float in [0.0, 1.0].                                     |
| `float_percentage`        | Validated Type  | Float in [0.0, 100.0].                                   |
| `float_latitude`          | Validated Type  | Float in [-90.0, 90.0].                                  |
| `float_longitude`         | Validated Type  | Float in [-180.0, 180.0].                                |
| `float_gt`                | Factory         | Float strictly greater than a threshold.                 |
| `float_ge`                | Factory         | Float greater than or equal to a threshold.               |
| `float_lt`                | Factory         | Float strictly less than a threshold.                     |
| `float_le`                | Factory         | Float less than or equal to a threshold.                  |
| `float_in_range`          | Factory         | Float within an inclusive range.                          |
"""