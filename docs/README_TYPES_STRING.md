<!-- README_TYPES_STRING.md -->
# 🔤 `presets/string` — Detailed Reference

Validated types for `str` — emptiness/blankness, character classes, casing,
common patterns (slug, email, URL, UUID, hex color), length, and value
restriction.

---

## 🧭 Table of Contents

**Emptiness & blankness**: [`str_empty`](#str_empty) · [`str_not_empty`](#str_not_empty) ·
[`str_blank`](#str_blank) · [`str_not_blank`](#str_not_blank) ·
[`str_whitespace`](#str_whitespace)

**Character classes**: [`str_alpha`](#str_alpha) · [`str_alnum`](#str_alnum) ·
[`str_digit`](#str_digit) · [`str_ascii`](#str_ascii) · [`str_printable`](#str_printable)

**Casing**: [`str_lower`](#str_lower) · [`str_upper`](#str_upper) · [`str_title`](#str_title)

**Patterns**: [`str_no_whitespace`](#str_no_whitespace) · [`str_single_line`](#str_single_line) ·
[`str_identifier`](#str_identifier) · [`str_slug`](#str_slug) ·
[`str_snake_case`](#str_snake_case) · [`str_email`](#str_email) · [`str_url`](#str_url) ·
[`str_uuid`](#str_uuid) · [`str_hex_color`](#str_hex_color)

**Parameterized**: [`str_length`](#str_length) · [`str_min_length`](#str_min_length) ·
[`str_max_length`](#str_max_length) · [`str_length_range`](#str_length_range) ·
[`str_starts_with`](#str_starts_with) · [`str_ends_with`](#str_ends_with) ·
[`str_contains`](#str_contains) · [`str_matches`](#str_matches) · [`str_one_of`](#str_one_of)

---

### `str_empty`

Validated type for an empty string.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `str`.
2. Value must be empty (length 0).

**Example usage:**
```python
@validate_call
def process(value: str_empty): ...
```

[▲ Back to top](#-table-of-contents)

---

### `str_not_empty`

Validated type for a non-empty string.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `str`.
2. Value must not be empty (length at least 1).

**Detailed description:**
A non-empty string may still consist entirely of whitespace (e.g. `"   "`). Use
`str_not_blank` if whitespace-only strings should also be rejected.

**Example usage:**
```python
@validate_call
def process(value: str_not_empty): ...
```

[▲ Back to top](#-table-of-contents)

---

### `str_blank`

Validated type for a blank string (empty or whitespace-only).

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `str`.
2. Value must be blank — empty or containing only whitespace characters.

**Example usage:**
```python
@validate_call
def process(value: str_blank): ...
```

[▲ Back to top](#-table-of-contents)

---

### `str_not_blank`

Validated type for a string that is neither empty nor whitespace-only.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `str`.
2. Value must not be blank (must contain at least one non-whitespace character).

**Example usage:**
```python
@validate_call
def process(value: str_not_blank): ...
```

[▲ Back to top](#-table-of-contents)

---

### `str_whitespace`

Validated type for a string consisting entirely of whitespace characters.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `str`.
2. Value must consist entirely of whitespace characters (and be non-empty).

**Example usage:**
```python
@validate_call
def process(value: str_whitespace): ...
```

[▲ Back to top](#-table-of-contents)

---

### `str_alpha`

Validated type for a string consisting entirely of alphabetic characters.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `str`.
2. Value must consist entirely of alphabetic characters.

**Example usage:**
```python
@validate_call
def process(value: str_alpha): ...
```

[▲ Back to top](#-table-of-contents)

---

### `str_alnum`

Validated type for a string consisting entirely of alphanumeric characters.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `str`.
2. Value must consist entirely of alphanumeric characters (letters and/or digits).

**Example usage:**
```python
@validate_call
def process(value: str_alnum): ...
```

[▲ Back to top](#-table-of-contents)

---

### `str_digit`

Validated type for a string consisting entirely of digit characters.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `str`.
2. Value must consist entirely of digit characters.

**Example usage:**
```python
@validate_call
def process(value: str_digit): ...
```

[▲ Back to top](#-table-of-contents)

---

### `str_ascii`

Validated type for a string consisting entirely of ASCII characters.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `str`.
2. Value must consist entirely of ASCII characters.

**Example usage:**
```python
@validate_call
def process(value: str_ascii): ...
```

[▲ Back to top](#-table-of-contents)

---

### `str_printable`

Validated type for a string consisting entirely of printable characters.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `str`.
2. Value must consist entirely of printable characters (no control characters).

**Example usage:**
```python
@validate_call
def process(value: str_printable): ...
```

[▲ Back to top](#-table-of-contents)

---

### `str_lower`

Validated type for a string that is entirely lowercase.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `str`.
2. Value must be entirely lowercase.

**Example usage:**
```python
@validate_call
def process(value: str_lower): ...
```

[▲ Back to top](#-table-of-contents)

---

### `str_upper`

Validated type for a string that is entirely uppercase.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `str`.
2. Value must be entirely uppercase.

**Example usage:**
```python
@validate_call
def process(value: str_upper): ...
```

[▲ Back to top](#-table-of-contents)

---

### `str_title`

Validated type for a string in title case.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `str`.
2. Value must be in title case (each word capitalized).

**Example usage:**
```python
@validate_call
def process(value: str_title): ...
```

[▲ Back to top](#-table-of-contents)

---

### `str_no_whitespace`

Validated type for a string containing no whitespace characters at all.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `str`.
2. Value must fully match the pattern `^\S*$` (no whitespace characters anywhere
   in the string).

**Example usage:**
```python
@validate_call
def process(value: str_no_whitespace): ...
```

[▲ Back to top](#-table-of-contents)

---

### `str_single_line`

Validated type for a single-line string (no line breaks).

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `str`.
2. Value must fully match the pattern `^[^\n\r]*$` (no newline or carriage
   return characters).

**Example usage:**
```python
@validate_call
def process(value: str_single_line): ...
```

[▲ Back to top](#-table-of-contents)

---

### `str_identifier`

Validated type for a string that is a valid Python identifier.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `str`.
2. Value must be a valid Python identifier (as per `str.isidentifier`).

**Example usage:**
```python
@validate_call
def process(value: str_identifier): ...
```

[▲ Back to top](#-table-of-contents)

---

### `str_slug`

Validated type for a URL-friendly slug string.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `str`.
2. Value must fully match the pattern `^[a-z0-9]+(?:-[a-z0-9]+)*$` — lowercase
   letters and digits, grouped into hyphen-separated segments (e.g.
   `my-blog-post`).

**Example usage:**
```python
@validate_call
def process(value: str_slug): ...
```

[▲ Back to top](#-table-of-contents)

---

### `str_snake_case`

Validated type for a snake_case string.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `str`.
2. Value must fully match the pattern `^[a-z][a-z0-9]*(?:_[a-z0-9]+)*$` — starts
   with a lowercase letter, followed by lowercase alphanumeric segments
   separated by underscores (e.g. `my_variable_name`).

**Example usage:**
```python
@validate_call
def process(value: str_snake_case): ...
```

[▲ Back to top](#-table-of-contents)

---

### `str_email`

Validated type for a string matching a basic email address shape.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `str`.
2. Value must fully match the pattern `^[^@\s]+@[^@\s]+\.[^@\s]+$`.

**Detailed description:**
This is a lightweight structural check (local-part @ domain . tld), not a full
RFC 5322 email validator — it accepts many strings that aren't real, deliverable
addresses and is meant to catch obviously malformed input rather than guarantee
validity.

**Example usage:**
```python
@validate_call
def process(value: str_email): ...
```

[▲ Back to top](#-table-of-contents)

---

### `str_url`

Validated type for a string matching a basic HTTP(S) URL shape.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `str`.
2. Value must fully match the pattern `^https?://[^\s]+$`.

**Detailed description:**
This only checks for an `http://` or `https://` prefix followed by non-whitespace
characters — it does not validate the URL's structure beyond that (e.g. malformed
hosts or paths may still pass).

**Example usage:**
```python
@validate_call
def process(value: str_url): ...
```

[▲ Back to top](#-table-of-contents)

---

### `str_uuid`

Validated type for a string in canonical UUID format.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `str`.
2. Value must fully match the canonical UUID pattern (8-4-4-4-12 hexadecimal
   digit groups separated by hyphens).

**Example usage:**
```python
@validate_call
def process(value: str_uuid): ...
```

[▲ Back to top](#-table-of-contents)

---

### `str_hex_color`

Validated type for a string in 6-digit hex color format.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `str`.
2. Value must fully match the pattern `^#[0-9a-fA-F]{6}$` (a `#` followed by
   exactly 6 hexadecimal digits).

**Example usage:**
```python
@validate_call
def process(value: str_hex_color): ...
```

[▲ Back to top](#-table-of-contents)

---

### `str_length`

Validated type for a string with an exact length.

**Init Params:**
* `exact` (*int*): The exact number of characters the string must contain.

**Validation pipeline:**
1. Value must be of type `str`.
2. Value's length must equal `exact`.

**Example usage:**
```python
FourChars = str_length(4)

@validate_call
def process(value: FourChars): ...
```

[▲ Back to top](#-table-of-contents)

---

### `str_min_length`

Validated type for a string with a minimum length.

**Init Params:**
* `min_length` (*int*): The minimum number of characters the string must contain
  (inclusive).

**Validation pipeline:**
1. Value must be of type `str`.
2. Value's length must be greater than or equal to `min_length`.

**Example usage:**
```python
NonTrivialStr = str_min_length(3)

@validate_call
def process(value: NonTrivialStr): ...
```

[▲ Back to top](#-table-of-contents)

---

### `str_max_length`

Validated type for a string with a maximum length.

**Init Params:**
* `max_length` (*int*): The maximum number of characters the string may contain
  (inclusive).

**Validation pipeline:**
1. Value must be of type `str`.
2. Value's length must be less than or equal to `max_length`.

**Example usage:**
```python
ShortStr = str_max_length(50)

@validate_call
def process(value: ShortStr): ...
```

[▲ Back to top](#-table-of-contents)

---

### `str_length_range`

Validated type for a string whose length falls within a given inclusive range.

**Init Params:**
* `min_length` (*int*): The inclusive minimum length.
* `max_length` (*int*): The inclusive maximum length.

**Validation pipeline:**
1. Value must be of type `str`.
2. Value's length must lie within the inclusive range [`min_length`, `max_length`].

**Example usage:**
```python
UsernameStr = str_length_range(3, 20)

@validate_call
def process(value: UsernameStr): ...
```

[▲ Back to top](#-table-of-contents)

---

### `str_starts_with`

Validated type for a string that must start with a given prefix.

**Init Params:**
* `prefix` (*str*): The required prefix.

**Validation pipeline:**
1. Value must be of type `str`.
2. Value must start with `prefix`.

**Example usage:**
```python
HttpsUrl = str_starts_with("https://")

@validate_call
def process(value: HttpsUrl): ...
```

[▲ Back to top](#-table-of-contents)

---

### `str_ends_with`

Validated type for a string that must end with a given suffix.

**Init Params:**
* `suffix` (*str*): The required suffix.

**Validation pipeline:**
1. Value must be of type `str`.
2. Value must end with `suffix`.

**Example usage:**
```python
PdfFilename = str_ends_with(".pdf")

@validate_call
def process(value: PdfFilename): ...
```

[▲ Back to top](#-table-of-contents)

---

### `str_contains`

Validated type for a string that must contain a given substring.

**Init Params:**
* `substring` (*str*): The substring that must be present somewhere in the value.

**Validation pipeline:**
1. Value must be of type `str`.
2. Value must contain `substring`.

**Example usage:**
```python
MustMentionError = str_contains("error")

@validate_call
def process(value: MustMentionError): ...
```

[▲ Back to top](#-table-of-contents)

---

### `str_matches`

Validated type for a string that must fully match a given regular expression
pattern.

**Init Params:**
* `pattern` (*str*): The regular expression the value must match.

**Validation pipeline:**
1. Value must be of type `str`.
2. Value must match `pattern`.

**Example usage:**
```python
DigitsOnly = str_matches(r"^\d+$")

@validate_call
def process(value: DigitsOnly): ...
```

[▲ Back to top](#-table-of-contents)

---

### `str_one_of`

Validated type for a string restricted to a fixed set of allowed values.

**Init Params:**
* `*options` (*str*): The set of values the string is allowed to equal.

**Validation pipeline:**
1. Value must be of type `str`.
2. Value must equal one of `options`.

**Example usage:**
```python
Status = str_one_of("pending", "active", "closed")

@validate_call
def process(value: Status): ...
```

[▲ Back to top](#-table-of-contents)

---

[⬅️ Back to main README](README_TYPES.md)