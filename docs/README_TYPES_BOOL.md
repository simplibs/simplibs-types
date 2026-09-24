<!-- README_TYPES_BOOL.md -->
# ✅ `presets/bool` — Detailed Reference

Validated types for `bool` — fixed truthy/falsy values.

---

## 🧭 Table of Contents

[`bool_true`](#bool_true) · [`bool_false`](#bool_false)

---

### `bool_true`

Validated type for a boolean that must be True.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `bool`.
2. Value must be `True`.

**Example usage:**
```python
@validate_call
def process(flag: bool_true): ...
```

[▲ Back to top](#-table-of-contents)

---

### `bool_false`

Validated type for a boolean that must be False.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `bool`.
2. Value must be `False`.

**Example usage:**
```python
@validate_call
def process(flag: bool_false): ...
```

[▲ Back to top](#-table-of-contents)

---

[⬅️ Back to main README](README_TYPES.md)