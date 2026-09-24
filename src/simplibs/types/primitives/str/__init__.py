# Direct:
from .direct.str_empty import str_empty
from .direct.str_not_empty import str_not_empty
from .direct.str_blank import str_blank
from .direct.str_not_blank import str_not_blank
from .direct.str_whitespace import str_whitespace
from .direct.str_alpha import str_alpha
from .direct.str_alnum import str_alnum
from .direct.str_digit import str_digit
from .direct.str_ascii import str_ascii
from .direct.str_printable import str_printable
from .direct.str_lower import str_lower
from .direct.str_upper import str_upper
from .direct.str_title import str_title
from .direct.str_no_whitespace import str_no_whitespace
from .direct.str_single_line import str_single_line
from .direct.str_identifier import str_identifier
from .direct.str_slug import str_slug
from .direct.str_snake_case import str_snake_case
from .direct.str_email import str_email
from .direct.str_url import str_url
from .direct.str_uuid import str_uuid
from .direct.str_hex_color import str_hex_color
# Parametric:
from .parametrized.str_length import str_length
from .parametrized.str_min_length import str_min_length
from .parametrized.str_max_length import str_max_length
from .parametrized.str_length_range import str_length_range
from .parametrized.str_starts_with import str_starts_with
from .parametrized.str_ends_with import str_ends_with
from .parametrized.str_contains import str_contains
from .parametrized.str_matches import str_matches
from .parametrized.str_one_of import str_one_of


_DESIGN_NOTES = """
# Str Presets Sub-Package

## Purpose
Validated types for `str` — emptiness/blankness, character classes,
casing, common patterns (slug, email, URL, UUID, hex color), length, and
value restriction.

## Internal Components Registry

| Component               | Type            | Description                                          |
| :-------------------------- | :-------------- | :--------------------------------------------------------- |
| `str_empty`                 | Validated Type  | Empty string.                                                |
| `str_not_empty`             | Validated Type  | Non-empty string.                                            |
| `str_blank`                 | Validated Type  | Empty or whitespace-only string.                             |
| `str_not_blank`             | Validated Type  | String with at least one non-whitespace character.           |
| `str_whitespace`            | Validated Type  | String consisting entirely of whitespace.                    |
| `str_alpha`                 | Validated Type  | String consisting entirely of letters.                       |
| `str_alnum`                 | Validated Type  | String consisting entirely of letters and/or digits.         |
| `str_digit`                 | Validated Type  | String consisting entirely of digits.                        |
| `str_ascii`                 | Validated Type  | String consisting entirely of ASCII characters.              |
| `str_printable`             | Validated Type  | String consisting entirely of printable characters.          |
| `str_lower`                 | Validated Type  | Entirely lowercase string.                                   |
| `str_upper`                 | Validated Type  | Entirely uppercase string.                                   |
| `str_title`                 | Validated Type  | Title-case string.                                            |
| `str_no_whitespace`         | Validated Type  | String with no whitespace characters at all.                 |
| `str_single_line`           | Validated Type  | String with no line breaks.                                  |
| `str_identifier`            | Validated Type  | String that is a valid Python identifier.                    |
| `str_slug`                  | Validated Type  | URL-friendly slug string.                                     |
| `str_snake_case`            | Validated Type  | snake_case string.                                            |
| `str_email`                 | Validated Type  | String matching a basic email address shape.                 |
| `str_url`                   | Validated Type  | String matching a basic HTTP(S) URL shape.                   |
| `str_uuid`                  | Validated Type  | String in canonical UUID format.                              |
| `str_hex_color`             | Validated Type  | String in 6-digit hex color format.                           |
| `str_length`                | Factory         | String with an exact length.                                  |
| `str_min_length`            | Factory         | String with a minimum length.                                 |
| `str_max_length`            | Factory         | String with a maximum length.                                 |
| `str_length_range`          | Factory         | String with a length in an inclusive range.                   |
| `str_starts_with`           | Factory         | String starting with a given prefix.                          |
| `str_ends_with`             | Factory         | String ending with a given suffix.                            |
| `str_contains`              | Factory         | String containing a given substring.                          |
| `str_matches`               | Factory         | String fully matching a regex pattern.                        |
| `str_one_of`                | Factory         | String restricted to a fixed set of allowed values.           |
"""