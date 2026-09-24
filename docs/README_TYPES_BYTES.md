<!-- README_TYPES_BYTES.md -->
# 📦 `presets/bytes` — Detailed Reference

Validated types for `bytes` — emptiness and length constraints.

---

## 🧭 Table of Contents

[`bytes_empty`](#bytes_empty) · [`bytes_not_empty`](#bytes_not_empty) ·
[`bytes_length`](#bytes_length) · [`bytes_min_length`](#bytes_min_length) ·
[`bytes_max_length`](#bytes_max_length) · [`bytes_length_range`](#bytes_length_range)

---

### `bytes_empty`

Validated type for empty bytes.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `bytes`.
2. Value must be empty (length 0).

**Example usage:**
```python
@validate_call
def process(value: bytes_empty): ...
```

[▲ Back to top](#-table-of-contents)

---

### `bytes_not_empty`

Validated type for non-empty bytes.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `bytes`.
2. Value must not be empty (length at least 1).

**Example usage:**
```python
@validate_call
def process(value: bytes_not_empty): ...
```

[▲ Back to top](#-table-of-contents)

---

### `bytes_length`

Validated type for bytes with an exact length.

**Init Params:**
* `exact` (*int*): The exact number of bytes the value must contain.

**Validation pipeline:**
1. Value must be of type `bytes`.
2. Value's length must equal `exact`.

**Example usage:**
```python
Md5Digest = bytes_length(16)

@validate_call
def process(value: Md5Digest): ...
```

[▲ Back to top](#-table-of-contents)

---

### `bytes_min_length`

Validated type for bytes with a minimum length.

**Init Params:**
* `min_length` (*int*): The minimum number of bytes the value must contain
  (inclusive).

**Validation pipeline:**
1. Value must be of type `bytes`.
2. Value's length must be greater than or equal to `min_length`.

**Example usage:**
```python
NonTrivialBytes = bytes_min_length(4)

@validate_call
def process(value: NonTrivialBytes): ...
```

[▲ Back to top](#-table-of-contents)

---

### `bytes_max_length`

Validated type for bytes with a maximum length.

**Init Params:**
* `max_length` (*int*): The maximum number of bytes the value may contain
  (inclusive).

**Validation pipeline:**
1. Value must be of type `bytes`.
2. Value's length must be less than or equal to `max_length`.

**Example usage:**
```python
SmallBytes = bytes_max_length(1024)

@validate_call
def process(value: SmallBytes): ...
```

[▲ Back to top](#-table-of-contents)

---

### `bytes_length_range`

Validated type for bytes whose length falls within a given inclusive range.

**Init Params:**
* `min_length` (*int*): The inclusive minimum length.
* `max_length` (*int*): The inclusive maximum length.

**Validation pipeline:**
1. Value must be of type `bytes`.
2. Value's length must lie within the inclusive range [`min_length`, `max_length`].

**Example usage:**
```python
TokenBytes = bytes_length_range(16, 32)

@validate_call
def process(value: TokenBytes): ...
```

[▲ Back to top](#-table-of-contents)

---

[⬅️ Back to main README](README_TYPES.md)