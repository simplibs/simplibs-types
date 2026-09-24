<!-- README_TYPES_INT.md -->
# 🔢 `presets/numeric` — Integer Reference

Validated types for `int` — sign, zero, parity, combined sign+parity, common
bounded ranges (byte ranges, percentages, ports, calendar/time fields), and
parameterized comparisons, equality, and divisibility.

---

## 🧭 Table of Contents

**Sign & zero**: [`int_positive`](#int_positive) · [`int_negative`](#int_negative) ·
[`int_non_negative`](#int_non_negative) · [`int_non_positive`](#int_non_positive) ·
[`int_zero`](#int_zero) · [`int_not_zero`](#int_not_zero)

**Parity**: [`int_even`](#int_even) · [`int_odd`](#int_odd) ·
[`int_positive_even`](#int_positive_even) · [`int_positive_odd`](#int_positive_odd) ·
[`int_non_negative_even`](#int_non_negative_even)

**Bounded ranges**: [`int_uint8`](#int_uint8) · [`int_int8`](#int_int8) ·
[`int_percentage`](#int_percentage) · [`int_port`](#int_port) ·
[`int_year`](#int_year) · [`int_month`](#int_month) ·
[`int_day_of_month`](#int_day_of_month) · [`int_hour`](#int_hour) ·
[`int_minute`](#int_minute) · [`int_second`](#int_second)

**Parameterized**: [`int_gt`](#int_gt) · [`int_ge`](#int_ge) · [`int_lt`](#int_lt) ·
[`int_le`](#int_le) · [`int_eq`](#int_eq) · [`int_ne`](#int_ne) ·
[`int_in_range`](#int_in_range) · [`int_divisible_by`](#int_divisible_by) ·
[`int_multiple_of`](#int_multiple_of)

---

### `int_positive`

Validated type for a positive integer (strictly greater than zero).

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `int`.
2. Value must be strictly greater than 0.

**Example usage:**
```python
@validate_call
def process(value: int_positive): ...
```

[▲ Back to top](#-table-of-contents)

---

### `int_negative`

Validated type for a negative integer (strictly less than zero).

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `int`.
2. Value must be strictly less than 0.

**Example usage:**
```python
@validate_call
def process(value: int_negative): ...
```

[▲ Back to top](#-table-of-contents)

---

### `int_non_negative`

Validated type for a non-negative integer (zero or positive).

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `int`.
2. Value must be greater than or equal to 0.

**Example usage:**
```python
@validate_call
def process(value: int_non_negative): ...
```

[▲ Back to top](#-table-of-contents)

---

### `int_non_positive`

Validated type for a non-positive integer (zero or negative).

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `int`.
2. Value must be less than or equal to 0.

**Example usage:**
```python
@validate_call
def process(value: int_non_positive): ...
```

[▲ Back to top](#-table-of-contents)

---

### `int_zero`

Validated type for an integer equal to zero.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `int`.
2. Value must be equal to 0.

**Example usage:**
```python
@validate_call
def process(value: int_zero): ...
```

[▲ Back to top](#-table-of-contents)

---

### `int_not_zero`

Validated type for an integer that is not zero.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `int`.
2. Value must not be equal to 0 (negated `is_zero`).

**Example usage:**
```python
@validate_call
def process(value: int_not_zero): ...
```

[▲ Back to top](#-table-of-contents)

---

### `int_even`

Validated type for an even integer.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `int`.
2. Value must be even (divisible by 2).

**Example usage:**
```python
@validate_call
def process(value: int_even): ...
```

[▲ Back to top](#-table-of-contents)

---

### `int_odd`

Validated type for an odd integer.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `int`.
2. Value must be odd (not divisible by 2).

**Example usage:**
```python
@validate_call
def process(value: int_odd): ...
```

[▲ Back to top](#-table-of-contents)

---

### `int_positive_even`

Validated type for a positive, even integer.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `int`.
2. Value must be strictly greater than 0.
3. Value must be even.

**Example usage:**
```python
@validate_call
def process(value: int_positive_even): ...
```

[▲ Back to top](#-table-of-contents)

---

### `int_positive_odd`

Validated type for a positive, odd integer.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `int`.
2. Value must be strictly greater than 0.
3. Value must be odd.

**Example usage:**
```python
@validate_call
def process(value: int_positive_odd): ...
```

[▲ Back to top](#-table-of-contents)

---

### `int_non_negative_even`

Validated type for a non-negative, even integer.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `int`.
2. Value must be greater than or equal to 0.
3. Value must be even.

**Example usage:**
```python
@validate_call
def process(value: int_non_negative_even): ...
```

[▲ Back to top](#-table-of-contents)

---

### `int_uint8`

Validated type for an integer in the unsigned 8-bit range.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `int`.
2. Value must lie within the inclusive range [0, 255].

**Example usage:**
```python
@validate_call
def process(value: int_uint8): ...
```

[▲ Back to top](#-table-of-contents)

---

### `int_int8`

Validated type for an integer in the signed 8-bit range.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `int`.
2. Value must lie within the inclusive range [-128, 127].

**Example usage:**
```python
@validate_call
def process(value: int_int8): ...
```

[▲ Back to top](#-table-of-contents)

---

### `int_percentage`

Validated type for an integer representing a percentage.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `int`.
2. Value must lie within the inclusive range [0, 100].

**Example usage:**
```python
@validate_call
def process(value: int_percentage): ...
```

[▲ Back to top](#-table-of-contents)

---

### `int_port`

Validated type for an integer representing a network port number.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `int`.
2. Value must lie within the inclusive range [0, 65535].

**Example usage:**
```python
@validate_call
def process(value: int_port): ...
```

[▲ Back to top](#-table-of-contents)

---

### `int_year`

Validated type for an integer representing a calendar year.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `int`.
2. Value must lie within the inclusive range [1, 9999].

**Example usage:**
```python
@validate_call
def process(value: int_year): ...
```

[▲ Back to top](#-table-of-contents)

---

### `int_month`

Validated type for an integer representing a calendar month.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `int`.
2. Value must lie within the inclusive range [1, 12].

**Example usage:**
```python
@validate_call
def process(value: int_month): ...
```

[▲ Back to top](#-table-of-contents)

---

### `int_day_of_month`

Validated type for an integer representing a day of the month.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `int`.
2. Value must lie within the inclusive range [1, 31].

**Detailed description:**
This only enforces the general [1, 31] bound — it does not account for month
length or leap years (e.g. it accepts 31 even for a month that only has 30 days).
Combine with additional application-level logic if calendar-accurate day
validation is required.

**Example usage:**
```python
@validate_call
def process(value: int_day_of_month): ...
```

[▲ Back to top](#-table-of-contents)

---

### `int_hour`

Validated type for an integer representing an hour (24-hour clock).

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `int`.
2. Value must lie within the inclusive range [0, 23].

**Example usage:**
```python
@validate_call
def process(value: int_hour): ...
```

[▲ Back to top](#-table-of-contents)

---

### `int_minute`

Validated type for an integer representing a minute.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `int`.
2. Value must lie within the inclusive range [0, 59].

**Example usage:**
```python
@validate_call
def process(value: int_minute): ...
```

[▲ Back to top](#-table-of-contents)

---

### `int_second`

Validated type for an integer representing a second.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `int`.
2. Value must lie within the inclusive range [0, 59].

**Detailed description:**
This does not account for leap seconds (value 60) — only the standard [0, 59]
range is accepted.

**Example usage:**
```python
@validate_call
def process(value: int_second): ...
```

[▲ Back to top](#-table-of-contents)

---

### `int_gt`

Validated type for an integer strictly greater than a given threshold.

**Init Params:**
* `threshold` (*int*): The exclusive lower bound.

**Validation pipeline:**
1. Value must be of type `int`.
2. Value must be strictly greater than `threshold`.

**Example usage:**
```python
AboveZero = int_gt(0)

@validate_call
def process(value: AboveZero): ...
```

[▲ Back to top](#-table-of-contents)

---

### `int_ge`

Validated type for an integer greater than or equal to a given threshold.

**Init Params:**
* `threshold` (*int*): The inclusive lower bound.

**Validation pipeline:**
1. Value must be of type `int`.
2. Value must be greater than or equal to `threshold`.

**Example usage:**
```python
AtLeastZero = int_ge(0)

@validate_call
def process(value: AtLeastZero): ...
```

[▲ Back to top](#-table-of-contents)

---

### `int_lt`

Validated type for an integer strictly less than a given threshold.

**Init Params:**
* `threshold` (*int*): The exclusive upper bound.

**Validation pipeline:**
1. Value must be of type `int`.
2. Value must be strictly less than `threshold`.

**Example usage:**
```python
BelowHundred = int_lt(100)

@validate_call
def process(value: BelowHundred): ...
```

[▲ Back to top](#-table-of-contents)

---

### `int_le`

Validated type for an integer less than or equal to a given threshold.

**Init Params:**
* `threshold` (*int*): The inclusive upper bound.

**Validation pipeline:**
1. Value must be of type `int`.
2. Value must be less than or equal to `threshold`.

**Example usage:**
```python
AtMostHundred = int_le(100)

@validate_call
def process(value: AtMostHundred): ...
```

[▲ Back to top](#-table-of-contents)

---

### `int_eq`

Validated type for an integer equal to a specific expected value.

**Init Params:**
* `expected` (*int*): The value the integer must equal.

**Validation pipeline:**
1. Value must be of type `int`.
2. Value must equal `expected`.

**Example usage:**
```python
MustBeSeven = int_eq(7)

@validate_call
def process(value: MustBeSeven): ...
```

[▲ Back to top](#-table-of-contents)

---

### `int_ne`

Validated type for an integer that must not equal a specific value.

**Init Params:**
* `forbidden` (*int*): The value the integer must not equal.

**Validation pipeline:**
1. Value must be of type `int`.
2. Value must not equal `forbidden`.

**Example usage:**
```python
NotThirteen = int_ne(13)

@validate_call
def process(value: NotThirteen): ...
```

[▲ Back to top](#-table-of-contents)

---

### `int_in_range`

Validated type for an integer within a given inclusive range.

**Init Params:**
* `min_val` (*int*): The inclusive lower bound.
* `max_val` (*int*): The inclusive upper bound.

**Validation pipeline:**
1. Value must be of type `int`.
2. Value must lie within the inclusive range [`min_val`, `max_val`].

**Example usage:**
```python
ScoreRange = int_in_range(0, 100)

@validate_call
def process(value: ScoreRange): ...
```

[▲ Back to top](#-table-of-contents)

---

### `int_divisible_by`

Validated type for an integer evenly divisible by a given divisor.

**Init Params:**
* `divisor` (*int*): The number the value must be evenly divisible by.

**Validation pipeline:**
1. Value must be of type `int`.
2. Value must be evenly divisible by `divisor` (no remainder).

**Example usage:**
```python
MultipleOfFive = int_divisible_by(5)

@validate_call
def process(value: MultipleOfFive): ...
```

[▲ Back to top](#-table-of-contents)

---

### `int_multiple_of`

Alias of `int_divisible_by` — validated type for an integer that is a multiple of
a given divisor.

**Init Params:**
* `divisor` (*int*): The number the value must be a multiple of.

**Validation pipeline:**
1. Value must be of type `int`.
2. Value must be evenly divisible by `divisor` (no remainder).

**Detailed description:**
Provided as a more naturally-worded alias — "multiple of" reads better at call
sites than "divisible by" in some contexts, but the underlying rule is identical.
See `int_divisible_by` for the canonical implementation.

**Example usage:**
```python
MultipleOfFive = int_multiple_of(5)

@validate_call
def process(value: MultipleOfFive): ...
```

[▲ Back to top](#-table-of-contents)

---

[⬅️ Back to main README](README_TYPES.md)