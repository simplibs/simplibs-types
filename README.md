# 🧩 `simplibs-types`

[![PyPI](https://img.shields.io/pypi/v/simplibs-types)](https://pypi.org/project/simplibs-types/)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/downloads/)
[![Licence](https://img.shields.io/badge/licence-MIT-green)](https://github.com/simplibs/simplibs-types/blob/main/LICENSE)

**Named, reusable validated types — a pure type-definition library, built on
[`simplibs-rules`](https://pypi.org/project/simplibs-rules/).**

A `Rule` from `simplibs-rules` answers "does this value satisfy me?". `simplibs-types`
provides a catalog of ready-made, documented, composed `Annotated` types for constraints
that come up again and again — instead of repeating `Annotated[int, greater_than(0)]`
by hand at every call site.

```python
from simplibs.types import int_positive, str_email
from simplibs.validate import validate_call

@validate_call
def register(age: int_positive, email: str_email) -> None:
    ...

register(25, "user@example.com")   # validated automatically
register(-5, "not-an-email")       # raises ValidationError
```

Every type ships with its own docstring, so it stays self-explanatory on hover — no
need to open a browser tab just to remember what `int_uint8` means.

---

## 🧭 The Core Philosophy

`simplibs-types` defines nothing new at the rule level — every constraint it enforces
comes straight from [`simplibs-rules`](https://pypi.org/project/simplibs-rules/). What
it adds is *naming*: a library of ready-made, documented, composed types for the
constraints that come up again and again (`int_positive`, `dict_not_empty`,
`str_email`, ...).

This is deliberately *not* a new validation mechanism: presets are built directly on top
of standard `Annotated[type_, *rules]`, and the actual checking happens inside
`simplibs-rules`' decomposition engine when invoked by runtime validators such as
`simplibs-validate`'s `validate_call`/`validate_dataclass`. `simplibs-types` itself is
purely a catalog of named type definitions — it ships no validation logic of its own
and depends solely on [`simplibs-rules`](https://pypi.org/project/simplibs-rules/).

---

## 📦 Installation

```bash
pip install simplibs-types
```

[`simplibs-rules`](https://pypi.org/project/simplibs-rules/) is installed automatically
as a dependency. Runtime validation decorators like `validate_call` or `validate_dataclass`
can be used via [`simplibs-validate`](https://pypi.org/project/simplibs-validate/).

---

## 🚀 Quick Start in 60 Seconds

### Level 1: Use a ready-made type

```python
from simplibs.types import int_positive
from simplibs.validate import validate_call

@validate_call
def set_quantity(amount: int_positive) -> None:
    ...

set_quantity(3)     # OK
set_quantity(-1)    # raises ValidationError
```

### Level 2: Use a parameterized preset

Some types take arguments and return a fresh `Annotated` construct each time they're
called:

```python
from simplibs.types import str_length_range

Username = str_length_range(3, 20)

@validate_call
def create_account(username: Username) -> None:
    ...
```

### Level 3: Define your own named type

```python
from typing import Annotated
from simplibs.rules import is_string, contains

CompanyEmail = Annotated[str, is_string & contains("@simplibs.dev")]

@validate_call
def notify(email: CompanyEmail) -> None:
    ...
```

---

## ⚠️ Type Checkers & Parameterized Types

All presets in `simplibs-types` are standard `typing.Annotated` constructs under the hood.

* **Parameterless types** (e.g., `int_positive`, `str_email`): Work seamlessly with static
  type checkers like Mypy or Pyright without any extra configuration.
* **Parameterized factory types** (e.g., `int_gt(0)`, `str_length_range(3, 20)`): Since they
  are generated dynamically at runtime via factory functions, static type checkers may report an issue such as:
  > `Invalid type annotation`

This is a **false positive** static analysis warning because dynamic `Annotated` instances returned by functions are evaluated at runtime, whereas static checkers expect static typing aliases.

### How to handle false positive warnings

1. **Ignore or suppress the warning:** You can add `# type: ignore` to line-level annotations.
2. **Re-wrap with `Annotated` (Recommended for clean static checking):**
   Wrap the parameterized factory result in `Annotated` once more on your side. The validation system automatically unpacks nested annotations:

```python
from typing import Annotated
from simplibs.types import str_length_range

# Avoids static type checker errors while preserving full runtime validation
Username = Annotated[str, str_length_range(3, 20)]
```

---

## 📖 Preset Catalog

Every preset below is built on `Annotated[type_, *rules]` and fully documented on hover.
Parameterless presets (`int_positive`, `dict_not_empty`, ...) are ready-made `Annotated`
constants; parameterized ones (`int_gt`, `str_length_range`, ...) are factory functions
that build a fresh `Annotated` construct per call.

### 1. Collections

Validated types for `dict`, `list`, `set`, and `tuple` — non-emptiness, length
constraints, uniqueness, and per-item rules.

| Type                    | Description                                     | Parameters         |
|--------------------------|--------------------------------------------------|----------------------|
| `dict_not_empty`        | Non-empty dictionary.                           | —                   |
| `dict_length`           | Dictionary with an exact number of items.       | `exact: int`        |
| `dict_min_length`       | Dictionary with a minimum number of items.      | `min_length: int`   |
| `dict_max_length`       | Dictionary with a maximum number of items.      | `max_length: int`   |
| `list_not_empty`        | Non-empty list.                                 | —                   |
| `list_unique`           | List with all unique items.                     | —                   |
| `list_unique_not_empty` | Non-empty list with all unique items.           | —                   |
| `list_of`               | List whose every item satisfies a given rule.   | `item_rule`         |
| `list_length`           | List with an exact number of items.             | `exact: int`        |
| `list_min_length`       | List with a minimum number of items.            | `min_length: int`   |
| `list_max_length`       | List with a maximum number of items.            | `max_length: int`   |
| `set_not_empty`         | Non-empty set.                                  | —                   |
| `set_of`                | Set whose every item satisfies a given rule.    | `item_rule`         |
| `set_length`            | Set with an exact number of items.              | `exact: int`        |
| `set_min_length`        | Set with a minimum number of items.             | `min_length: int`   |
| `set_max_length`        | Set with a maximum number of items.             | `max_length: int`   |
| `tuple_not_empty`       | Non-empty tuple.                                | —                   |
| `tuple_of`              | Tuple whose every item satisfies a given rule.  | `item_rule`         |
| `tuple_length`          | Tuple with an exact number of items.            | `exact: int`        |
| `tuple_min_length`      | Tuple with a minimum number of items.           | `min_length: int`   |
| `tuple_max_length`      | Tuple with a maximum number of items.           | `max_length: int`   |

➡️ [Full reference (README_TYPES_COLLECTIONS)](https://github.com/simplibs/simplibs-types/blob/main/docs/README_TYPES_COLLECTIONS.md)

### 2. Numeric

Validated types for `int`, `float`, and the `int | float` union (`number_*`) — sign,
zero, parity, ranges, and special float states (NaN, infinity).

| Type                     | Description                                       | Parameters                       |
|----------------------------|------------------------------------------------------|-------------------------------------|
| `int_positive`           | Positive integer.                                  | —                                 |
| `int_negative`           | Negative integer.                                  | —                                 |
| `int_non_negative`       | Non-negative integer.                              | —                                 |
| `int_non_positive`       | Non-positive integer.                              | —                                 |
| `int_zero`               | Integer equal to zero.                             | —                                 |
| `int_not_zero`           | Integer not equal to zero.                         | —                                 |
| `int_even`               | Even integer.                                      | —                                 |
| `int_odd`                | Odd integer.                                       | —                                 |
| `int_positive_even`      | Positive, even integer.                            | —                                 |
| `int_positive_odd`       | Positive, odd integer.                             | —                                 |
| `int_non_negative_even`  | Non-negative, even integer.                        | —                                 |
| `int_uint8`              | Integer in unsigned 8-bit range [0, 255].          | —                                 |
| `int_int8`               | Integer in signed 8-bit range [-128, 127].         | —                                 |
| `int_percentage`         | Integer percentage [0, 100].                       | —                                 |
| `int_port`               | Integer network port [0, 65535].                   | —                                 |
| `int_year`               | Integer calendar year [1, 9999].                   | —                                 |
| `int_month`              | Integer calendar month [1, 12].                    | —                                 |
| `int_day_of_month`       | Integer day of month [1, 31].                      | —                                 |
| `int_hour`               | Integer hour, 24h clock [0, 23].                   | —                                 |
| `int_minute`             | Integer minute [0, 59].                            | —                                 |
| `int_second`             | Integer second [0, 59].                            | —                                 |
| `int_gt` / `int_ge`      | Integer greater than / or equal to a threshold.    | `threshold: int`                  |
| `int_lt` / `int_le`      | Integer less than / or equal to a threshold.       | `threshold: int`                  |
| `int_eq` / `int_ne`      | Integer equal / not equal to a specific value.     | `expected`/`forbidden: int`       |
| `int_in_range`           | Integer within an inclusive range.                 | `min_val: int, max_val: int`      |
| `int_divisible_by`       | Integer evenly divisible by a divisor.             | `divisor: int`                    |
| `int_multiple_of`        | Alias of `int_divisible_by`.                       | `divisor: int`                    |
| `float_positive`         | Positive float.                                    | —                                 |
| `float_negative`         | Negative float.                                    | —                                 |
| `float_non_negative`     | Non-negative float.                                | —                                 |
| `float_non_positive`     | Non-positive float.                                | —                                 |
| `float_zero`             | Float equal to zero.                               | —                                 |
| `float_not_zero`         | Float not equal to zero.                           | —                                 |
| `float_finite`           | Finite float (not NaN, not infinite).              | —                                 |
| `float_not_nan`          | Float that is not NaN.                             | —                                 |
| `float_not_infinite`     | Float that is not +/-infinity.                     | —                                 |
| `float_probability`      | Float in [0.0, 1.0].                               | —                                 |
| `float_percentage`       | Float in [0.0, 100.0].                             | —                                 |
| `float_latitude`         | Float in [-90.0, 90.0].                            | —                                 |
| `float_longitude`        | Float in [-180.0, 180.0].                          | —                                 |
| `float_gt` / `float_ge`  | Float greater than / or equal to a threshold.      | `threshold: float`                |
| `float_lt` / `float_le`  | Float less than / or equal to a threshold.         | `threshold: float`                |
| `float_in_range`         | Float within an inclusive range.                   | `min_val: float, max_val: float`  |
| `number_positive`        | Positive number (int or float).                    | —                                 |
| `number_negative`        | Negative number (int or float).                    | —                                 |
| `number_non_negative`    | Non-negative number (int or float).                | —                                 |
| `number_non_positive`    | Non-positive number (int or float).                | —                                 |
| `number_zero`            | Number equal to zero.                              | —                                 |
| `number_not_zero`        | Number not equal to zero.                          | —                                 |
| `number_finite`          | Finite number (int or float).                      | —                                 |
| `number_in_range`        | Number within an inclusive range.                  | `min_val, max_val: Any`           |

➡️ [Full reference — integers (README_TYPES_INT)](https://github.com/simplibs/simplibs-types/blob/main/docs/README_TYPES_INT.md)  
➡️ [Full reference — floats & numbers (README_TYPES_FLOAT)](https://github.com/simplibs/simplibs-types/blob/main/docs/README_TYPES_FLOAT.md)  

### 3. Boolean

| Type         | Description                  | Parameters |
|---------------|--------------------------------|------------|
| `bool_true`  | Boolean that must be `True`. | —          |
| `bool_false` | Boolean that must be `False`.| —          |

➡️ [Full reference (README_TYPES_BOOL)](https://github.com/simplibs/simplibs-types/blob/main/docs/README_TYPES_BOOL.md)  

### 4. String

Validated types for `str` — emptiness/blankness, character classes, casing, patterns,
length, and value restriction.

| Type                | Description                                          | Parameters                          |
|-----------------------|---------------------------------------------------------|----------------------------------------|
| `str_empty`         | Empty string.                                          | —                                    |
| `str_not_empty`     | Non-empty string.                                      | —                                    |
| `str_blank`         | Empty or whitespace-only string.                       | —                                    |
| `str_not_blank`     | String with at least one non-whitespace character.     | —                                    |
| `str_whitespace`    | String consisting entirely of whitespace.              | —                                    |
| `str_alpha`         | String consisting entirely of letters.                 | —                                    |
| `str_alnum`         | String consisting entirely of letters and/or digits.   | —                                    |
| `str_digit`         | String consisting entirely of digits.                  | —                                    |
| `str_ascii`         | String consisting entirely of ASCII characters.        | —                                    |
| `str_printable`     | String consisting entirely of printable characters.    | —                                    |
| `str_lower`         | Entirely lowercase string.                             | —                                    |
| `str_upper`         | Entirely uppercase string.                             | —                                    |
| `str_title`         | Title-case string.                                     | —                                    |
| `str_no_whitespace` | String with no whitespace characters at all.           | —                                    |
| `str_single_line`   | String with no line breaks.                            | —                                    |
| `str_identifier`    | String that is a valid Python identifier.              | —                                    |
| `str_slug`          | URL-friendly slug string.                               | —                                    |
| `str_snake_case`    | snake_case string.                                     | —                                    |
| `str_email`         | String matching a basic email address shape.           | —                                    |
| `str_url`           | String matching a basic HTTP(S) URL shape.             | —                                    |
| `str_uuid`          | String in canonical UUID format.                       | —                                    |
| `str_hex_color`     | String in 6-digit hex color format.                    | —                                    |
| `str_length`        | String with an exact length.                           | `exact: int`                         |
| `str_min_length`    | String with a minimum length.                          | `min_length: int`                    |
| `str_max_length`    | String with a maximum length.                          | `max_length: int`                    |
| `str_length_range`  | String with a length in an inclusive range.            | `min_length: int, max_length: int`   |
| `str_starts_with`   | String starting with a given prefix.                   | `prefix: str`                        |
| `str_ends_with`     | String ending with a given suffix.                     | `suffix: str`                        |
| `str_contains`      | String containing a given substring.                   | `substring: str`                     |
| `str_matches`       | String fully matching a regex pattern.                 | `pattern: str`                       |
| `str_one_of`        | String restricted to a fixed set of allowed values.    | `*options: str`                      |

➡️ [Full reference (README_TYPES_STRING)](https://github.com/simplibs/simplibs-types/blob/main/docs/README_TYPES_STRING.md)  

### 5. Bytes

| Type                 | Description                                | Parameters                        |
|------------------------|-----------------------------------------------|--------------------------------------|
| `bytes_empty`        | Empty bytes.                               | —                                  |
| `bytes_not_empty`    | Non-empty bytes.                           | —                                  |
| `bytes_length`       | Bytes with an exact length.                | `exact: int`                       |
| `bytes_min_length`   | Bytes with a minimum length.               | `min_length: int`                  |
| `bytes_max_length`   | Bytes with a maximum length.               | `max_length: int`                  |
| `bytes_length_range` | Bytes with a length in an inclusive range. | `min_length: int, max_length: int` |

➡️ [Full reference (README_TYPES_BYTES)](https://github.com/simplibs/simplibs-types/blob/main/docs/README_TYPES_BYTES.md)  

---

## 💡 Why every type has a docstring

Every preset — parameterless constant or parameterized factory alike — carries a
docstring describing what it validates, its parameters (if any), and a usage example.
That's a deliberate design choice: since `Annotated[type_, *rules]` doesn't surface its
constraints in a hover tooltip on its own, the docstring is what makes `int_uint8` or
`str_email` self-explanatory at the call site, without needing to open documentation or
jump to the definition.

---

## 🔗 Related libraries

* **[`simplibs-rules`](https://pypi.org/project/simplibs-rules/)** — the `Rule` base
  class and every predicate (`is_integer`, `greater_than`, `contains`, ...) that
  presets here are composed from.
* **[`simplibs-validate`](https://pypi.org/project/simplibs-validate/)** — provides
  runtime execution helpers (`validate()`, `validate_call`, `validate_dataclass`) to
  enforce these types in functions or dataclasses at runtime.

---

## ☯️ About simplibs

All libraries in the **simplibs** (Simple Libraries) ecosystem share a common
engineering philosophy:

* **Dyslexia-friendly:**
We actively minimize cognitive load. Code is atomized into small, self-contained units,
files are named directly after the logical task they perform, and explanations describe
*why* something is designed, not just *what* it is.
* **Programmer's Zen:**
Nothing should be missing, and nothing should be superfluous. We value clean execution
paths and robust, understandable code architectures over rushed, messy feature sets.
* **Defensive Style:**
We actively anticipate edge cases and failure modes so that only safe operational paths
remain. Our code is built to degrade gracefully rather than crash unexpectedly.
* **Minimalism:**
Find the most direct path to the goal in as few operational steps as possible without
taking shortcuts on safety, readability, or completeness.
* **Code as Craft:**
Code should be pleasant to look at, readable at a glance, and evoke structural harmony.
We treat software engineering as a precision trade.

---

### 🤝 Contributing & Community

This is an **open-source project** built with love and care. We strongly believe in
community collaboration and welcome any feedback, bug reports, or feature ideas!

* **Want to contribute?** Feel free to open an Issue or submit a Pull Request.
* **Want to get in touch?** If you'd like to discuss the project further, collaborate,
  or just say hello, feel free to open a GitHub Issue or start a Discussion.

---

### 📝 License

This library is released under the **MIT License**. Build great things!

---

[▲ Back to Top](#-simplibs-types)