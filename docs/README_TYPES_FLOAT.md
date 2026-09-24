<!-- README_TYPES_FLOAT_NUMBER.md -->
# 🔢 `presets/numeric` — Float & Number Reference

Validated types for `float` (sign, zero, special IEEE-754 states, common bounded
ranges) and for the `int | float` union (`number_*` — sign, zero, finiteness, and
generic ranges shared by both numeric types).

---

## 🧭 Table of Contents

**float — sign & zero**: [`float_positive`](#float_positive) ·
[`float_negative`](#float_negative) · [`float_non_negative`](#float_non_negative) ·
[`float_non_positive`](#float_non_positive) · [`float_zero`](#float_zero) ·
[`float_not_zero`](#float_not_zero)

**float — special states**: [`float_finite`](#float_finite) ·
[`float_not_nan`](#float_not_nan) · [`float_not_infinite`](#float_not_infinite)

**float — bounded ranges**: [`float_probability`](#float_probability) ·
[`float_percentage`](#float_percentage) · [`float_latitude`](#float_latitude) ·
[`float_longitude`](#float_longitude)

**float — parameterized**: [`float_gt`](#float_gt) · [`float_ge`](#float_ge) ·
[`float_lt`](#float_lt) · [`float_le`](#float_le) ·
[`float_in_range`](#float_in_range)

**number (int | float)**: [`number_positive`](#number_positive) ·
[`number_negative`](#number_negative) · [`number_non_negative`](#number_non_negative) ·
[`number_non_positive`](#number_non_positive) · [`number_zero`](#number_zero) ·
[`number_not_zero`](#number_not_zero) · [`number_finite`](#number_finite) ·
[`number_in_range`](#number_in_range)

---

### `float_positive`

Validated type for a positive float (strictly greater than zero).

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `float`.
2. Value must be strictly greater than 0.0.

**Example usage:**
```python
@validate_call
def process(value: float_positive): ...
```

[▲ Back to top](#-table-of-contents)

---

### `float_negative`

Validated type for a negative float (strictly less than zero).

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `float`.
2. Value must be strictly less than 0.0.

**Example usage:**
```python
@validate_call
def process(value: float_negative): ...
```

[▲ Back to top](#-table-of-contents)

---

### `float_non_negative`

Validated type for a non-negative float (zero or positive).

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `float`.
2. Value must be greater than or equal to 0.0.

**Example usage:**
```python
@validate_call
def process(value: float_non_negative): ...
```

[▲ Back to top](#-table-of-contents)

---

### `float_non_positive`

Validated type for a non-positive float (zero or negative).

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `float`.
2. Value must be less than or equal to 0.0.

**Example usage:**
```python
@validate_call
def process(value: float_non_positive): ...
```

[▲ Back to top](#-table-of-contents)

---

### `float_zero`

Validated type for a float equal to zero.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `float`.
2. Value must be equal to 0.

**Example usage:**
```python
@validate_call
def process(value: float_zero): ...
```

[▲ Back to top](#-table-of-contents)

---

### `float_not_zero`

Validated type for a float that is not zero.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `float`.
2. Value must not be equal to 0 (negated `is_zero`).

**Example usage:**
```python
@validate_call
def process(value: float_not_zero): ...
```

[▲ Back to top](#-table-of-contents)

---

### `float_finite`

Validated type for a finite float (neither NaN nor infinite).

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `float`.
2. Value must be finite (not NaN and not +/-infinity).

**Example usage:**
```python
@validate_call
def process(value: float_finite): ...
```

[▲ Back to top](#-table-of-contents)

---

### `float_not_nan`

Validated type for a float that is not NaN.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `float`.
2. Value must not be NaN (negated `is_nan`).

**Detailed description:**
Unlike `float_finite`, this only excludes NaN — +/-infinity is still accepted.
Use `float_finite` if both NaN and infinity should be rejected.

**Example usage:**
```python
@validate_call
def process(value: float_not_nan): ...
```

[▲ Back to top](#-table-of-contents)

---

### `float_not_infinite`

Validated type for a float that is not +/-infinity.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `float`.
2. Value must not be infinite (negated `is_infinity`).

**Detailed description:**
Unlike `float_finite`, this only excludes +/-infinity — NaN is still accepted.
Use `float_finite` if both NaN and infinity should be rejected.

**Example usage:**
```python
@validate_call
def process(value: float_not_infinite): ...
```

[▲ Back to top](#-table-of-contents)

---

### `float_probability`

Validated type for a float representing a probability.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `float`.
2. Value must lie within the inclusive range [0.0, 1.0].

**Example usage:**
```python
@validate_call
def process(value: float_probability): ...
```

[▲ Back to top](#-table-of-contents)

---

### `float_percentage`

Validated type for a float representing a percentage.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `float`.
2. Value must lie within the inclusive range [0.0, 100.0].

**Example usage:**
```python
@validate_call
def process(value: float_percentage): ...
```

[▲ Back to top](#-table-of-contents)

---

### `float_latitude`

Validated type for a float representing a geographic latitude.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `float`.
2. Value must lie within the inclusive range [-90.0, 90.0].

**Example usage:**
```python
@validate_call
def process(value: float_latitude): ...
```

[▲ Back to top](#-table-of-contents)

---

### `float_longitude`

Validated type for a float representing a geographic longitude.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `float`.
2. Value must lie within the inclusive range [-180.0, 180.0].

**Example usage:**
```python
@validate_call
def process(value: float_longitude): ...
```

[▲ Back to top](#-table-of-contents)

---

### `float_gt`

Validated type for a float strictly greater than a given threshold.

**Init Params:**
* `threshold` (*float*): The exclusive lower bound.

**Validation pipeline:**
1. Value must be of type `float`.
2. Value must be strictly greater than `threshold`.

**Example usage:**
```python
AboveZero = float_gt(0.0)

@validate_call
def process(value: AboveZero): ...
```

[▲ Back to top](#-table-of-contents)

---

### `float_ge`

Validated type for a float greater than or equal to a given threshold.

**Init Params:**
* `threshold` (*float*): The inclusive lower bound.

**Validation pipeline:**
1. Value must be of type `float`.
2. Value must be greater than or equal to `threshold`.

**Example usage:**
```python
AtLeastZero = float_ge(0.0)

@validate_call
def process(value: AtLeastZero): ...
```

[▲ Back to top](#-table-of-contents)

---

### `float_lt`

Validated type for a float strictly less than a given threshold.

**Init Params:**
* `threshold` (*float*): The exclusive upper bound.

**Validation pipeline:**
1. Value must be of type `float`.
2. Value must be strictly less than `threshold`.

**Example usage:**
```python
BelowHundred = float_lt(100.0)

@validate_call
def process(value: BelowHundred): ...
```

[▲ Back to top](#-table-of-contents)

---

### `float_le`

Validated type for a float less than or equal to a given threshold.

**Init Params:**
* `threshold` (*float*): The inclusive upper bound.

**Validation pipeline:**
1. Value must be of type `float`.
2. Value must be less than or equal to `threshold`.

**Example usage:**
```python
AtMostHundred = float_le(100.0)

@validate_call
def process(value: AtMostHundred): ...
```

[▲ Back to top](#-table-of-contents)

---

### `float_in_range`

Validated type for a float within a given inclusive range.

**Init Params:**
* `min_val` (*float*): The inclusive lower bound.
* `max_val` (*float*): The inclusive upper bound.

**Validation pipeline:**
1. Value must be of type `float`.
2. Value must lie within the inclusive range [`min_val`, `max_val`].

**Example usage:**
```python
UnitRange = float_in_range(0.0, 1.0)

@validate_call
def process(value: UnitRange): ...
```

[▲ Back to top](#-table-of-contents)

---

### `number_positive`

Validated type for a positive number (int or float, strictly greater than zero).

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `int` or `float` (`Number`).
2. Value must be strictly greater than 0.

**Example usage:**
```python
@validate_call
def process(value: number_positive): ...
```

[▲ Back to top](#-table-of-contents)

---

### `number_negative`

Validated type for a negative number (int or float, strictly less than zero).

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `int` or `float` (`Number`).
2. Value must be strictly less than 0.

**Example usage:**
```python
@validate_call
def process(value: number_negative): ...
```

[▲ Back to top](#-table-of-contents)

---

### `number_non_negative`

Validated type for a non-negative number (int or float, zero or positive).

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `int` or `float` (`Number`).
2. Value must be greater than or equal to 0.

**Example usage:**
```python
@validate_call
def process(value: number_non_negative): ...
```

[▲ Back to top](#-table-of-contents)

---

### `number_non_positive`

Validated type for a non-positive number (int or float, zero or negative).

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `int` or `float` (`Number`).
2. Value must be less than or equal to 0.

**Example usage:**
```python
@validate_call
def process(value: number_non_positive): ...
```

[▲ Back to top](#-table-of-contents)

---

### `number_zero`

Validated type for a number (int or float) equal to zero.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `int` or `float` (`Number`).
2. Value must be equal to 0.

**Example usage:**
```python
@validate_call
def process(value: number_zero): ...
```

[▲ Back to top](#-table-of-contents)

---

### `number_not_zero`

Validated type for a number (int or float) that is not zero.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `int` or `float` (`Number`).
2. Value must not be equal to 0 (negated `is_zero`).

**Example usage:**
```python
@validate_call
def process(value: number_not_zero): ...
```

[▲ Back to top](#-table-of-contents)

---

### `number_finite`

Validated type for a finite number (int or float, neither NaN nor infinite).

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `int` or `float` (`Number`).
2. Value must be finite (not NaN and not +/-infinity).

**Detailed description:**
Relevant mainly for the `float` case, since plain `int` values are always finite
by construction — this rule is what makes `number_finite` meaningfully stricter
than the bare `Number` type when a `float` is passed.

**Example usage:**
```python
@validate_call
def process(value: number_finite): ...
```

[▲ Back to top](#-table-of-contents)

---

### `number_in_range`

Validated type for a number (int or float) within a given inclusive range.

**Init Params:**
* `min_val` (*Any*): The inclusive lower bound.
* `max_val` (*Any*): The inclusive upper bound.

**Validation pipeline:**
1. Value must be of type `int` or `float` (`Number`).
2. Value must lie within the inclusive range [`min_val`, `max_val`].

**Example usage:**
```python
ScoreRange = number_in_range(0, 100)

@validate_call
def process(value: ScoreRange): ...
```

[▲ Back to top](#-table-of-contents)

---

[⬅️ Back to main README](README_TYPES.md)