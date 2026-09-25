# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

---

## [0.2.0] - 2026-09-25

### 🔄 Changed

#### Refactoring type definitions to standard `Annotated`

* **Native Static Typing**: All parameterless preset types were refactored
  from `validated_type(...)` calls to native `typing.Annotated[...]` constructs.
  IDEs and static type checkers (PyCharm, Mypy, Pyright) now natively recognize
  these aliases as valid types for autocomplete and type hinting without warnings.
* **Redundant Type Validation Removal**: Simplified metadata rules in `Annotated`
  definitions. The validation engine (`simplibs-validate`) automatically
  inspects the target type argument of `Annotated[T, ...]` and prepends an
  implicit `IsInstance(T)` check. Consequently, metadata rules no longer need
  to re-verify the underlying base type, avoiding duplicate checks.

#### Dependencies

* **Lightweight Production Runtime**: Removed `simplibs-validate` and
  `simplibs-exception` from runtime dependencies. The core library now strictly
  depends only on `simplibs-rules`, drastically reducing package weight and
  footprint.
* `simplibs-validate` has been moved to `dev` dependencies solely to support
  the test suite (`pytest`).

### 📋 Improved

#### Parameterized Types Usage & Hints

* Parameterized type factories (functions returning `Annotated[T, ...]`) now
  use standard `Annotated` return types.
* *Note on Type Checker Behavior*: Assigning the return value of a function to
  a variable (e.g., `Triplet = tuple_length(3)`) and using it directly as a
  type annotation in signature definitions can trigger static type analyzer
  warnings (`Invalid type annotation`).
  * To circumvent this in user projects, you can either suppress the warning
    via `# type: ignore[valid-type]`, use the function call directly inside
    the annotation `@validate_call def process(x: tuple_length(3)): ...`, or
    wrap it into a secondary native `Annotated` alias (e.g., `Triplet =
    Annotated[tuple, has_length(3)]`).
  * The `simplibs-validate` engine seamlessly unrolls and resolves nested
    `Annotated` metadata structures at runtime.

---

## [0.1.0] - 2026-09-24

### ✨ Added

#### Preset Types — Collections (`simplibs.types.presets.collections`)

* `dict`: `dict_not_empty`, `dict_length`, `dict_min_length`, `dict_max_length`
* `list`: `list_not_empty`, `list_unique`, `list_unique_not_empty`, `list_of`,
  `list_length`, `list_min_length`, `list_max_length`
* `set`: `set_not_empty`, `set_of`, `set_length`, `set_min_length`, `set_max_length`
* `tuple`: `tuple_not_empty`, `tuple_of`, `tuple_length`, `tuple_min_length`,
  `tuple_max_length`
* `*_of` factories apply a given item rule to every element via `for_each`, and accept
  another validated type as a nested annotation

#### Preset Types — Numeric (`simplibs.types.presets.numeric`)

* `int`: sign/zero (`int_positive`, `int_negative`, `int_non_negative`,
  `int_non_positive`, `int_zero`, `int_not_zero`), parity (`int_even`, `int_odd`,
  `int_positive_even`, `int_positive_odd`, `int_non_negative_even`), bounded ranges
  (`int_uint8`, `int_int8`, `int_percentage`, `int_port`, `int_year`, `int_month`,
  `int_day_of_month`, `int_hour`, `int_minute`, `int_second`), and parameterized
  comparisons/equality/divisibility (`int_gt`, `int_ge`, `int_lt`, `int_le`, `int_eq`,
  `int_ne`, `int_in_range`, `int_divisible_by`, `int_multiple_of`)
* `float`: sign/zero, special IEEE-754 states (`float_finite`, `float_not_nan`,
  `float_not_infinite`), bounded ranges (`float_probability`, `float_percentage`,
  `float_latitude`, `float_longitude`), and parameterized comparisons/range
  (`float_gt`, `float_ge`, `float_lt`, `float_le`, `float_in_range`)
* `int | float` union: `number_positive`, `number_negative`, `number_non_negative`,
  `number_non_positive`, `number_zero`, `number_not_zero`, `number_finite`,
  `number_in_range`

#### Preset Types — Boolean (`simplibs.types.presets.bool`)

* `bool_true`, `bool_false`

#### Preset Types — String (`simplibs.types.presets.string`)

* Emptiness/blankness: `str_empty`, `str_not_empty`, `str_blank`, `str_not_blank`,
  `str_whitespace`
* Character classes & casing: `str_alpha`, `str_alnum`, `str_digit`, `str_ascii`,
  `str_printable`, `str_lower`, `str_upper`, `str_title`
* Shape: `str_no_whitespace`, `str_single_line`, `str_identifier`, `str_slug`,
  `str_snake_case`, `str_email`, `str_url`, `str_uuid`, `str_hex_color`
* Length: `str_length`, `str_min_length`, `str_max_length`, `str_length_range`
* Content: `str_starts_with`, `str_ends_with`, `str_contains`, `str_matches`,
  `str_one_of`

#### Preset Types — Bytes (`simplibs.types.presets.bytes`)

* `bytes_empty`, `bytes_not_empty`, `bytes_length`, `bytes_min_length`,
  `bytes_max_length`, `bytes_length_range`

#### Documentation

* Every preset — parameterless constant or parameterized factory alike — ships its own
  docstring (validation pipeline + usage example), so types stay self-explanatory on
  hover without needing to open external documentation
* Full reference documentation per category (collections, numeric, bool, string,
  bytes)
* Main README with the full preset catalog

#### Dependencies

* `simplibs-rules` — every predicate (`is_integer`, `greater_than`, `contains`, ...)
  and the `Rule` base class that presets in this library are composed from
* `simplibs-validate` — underlying validation engine and `validated_type` constructor

---

## Legend

* 🔄 **Changed** — modifications to existing functionality
* ✨ **Added** — new features and components
* 🐛 **Fixed** — bug fixes
* 📋 **Improved** — enhancements to existing features
* ⚠️ **Deprecated** — deprecated functionality (not used yet in this project)
* 🗑️ **Removed** — removed functionality (not used yet in this project)