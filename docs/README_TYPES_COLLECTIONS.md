<!-- README_TYPES_COLLECTIONS.md -->
# 📚 `presets/collections` — Detailed Reference

Validated types for the four built-in container types (`dict`, `list`, `set`, `tuple`).
Covers non-emptiness, length constraints, item uniqueness, and per-item validation via
`*_of` factories. Each card below is the type's full docstring; grouped by container.

---

## 🧭 Table of Contents

**dict**: [`dict_not_empty`](#dict_not_empty) · [`dict_length`](#dict_length) ·
[`dict_min_length`](#dict_min_length) · [`dict_max_length`](#dict_max_length)

**list**: [`list_not_empty`](#list_not_empty) · [`list_unique`](#list_unique) ·
[`list_unique_not_empty`](#list_unique_not_empty) · [`list_of`](#list_of) ·
[`list_length`](#list_length) · [`list_min_length`](#list_min_length) ·
[`list_max_length`](#list_max_length)

**set**: [`set_not_empty`](#set_not_empty) · [`set_of`](#set_of) ·
[`set_length`](#set_length) · [`set_min_length`](#set_min_length) ·
[`set_max_length`](#set_max_length)

**tuple**: [`tuple_not_empty`](#tuple_not_empty) · [`tuple_of`](#tuple_of) ·
[`tuple_length`](#tuple_length) · [`tuple_min_length`](#tuple_min_length) ·
[`tuple_max_length`](#tuple_max_length)

---

### `dict_not_empty`

Validated type for a non-empty dictionary.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `dict`.
2. Value must not be empty (must contain at least one item).

**Example usage:**
```python
@validate_call
def process(data: dict_not_empty): ...
```

[▲ Back to top](#-table-of-contents)

---

### `dict_length`

Validated type for a dictionary with an exact number of items.

**Init Params:**
* `exact` (*int*): The exact number of key-value pairs the dictionary must contain.

**Validation pipeline:**
1. Value must be of type `dict`.
2. Value's length must equal `exact`.

**Example usage:**
```python
ThreeItemDict = dict_length(3)

@validate_call
def process(data: ThreeItemDict): ...
```

[▲ Back to top](#-table-of-contents)

---

### `dict_min_length`

Validated type for a dictionary with a minimum number of items.

**Init Params:**
* `min_length` (*int*): The minimum number of key-value pairs the dictionary must
  contain (inclusive).

**Validation pipeline:**
1. Value must be of type `dict`.
2. Value's length must be greater than or equal to `min_length`.

**Example usage:**
```python
NonTrivialDict = dict_min_length(2)

@validate_call
def process(data: NonTrivialDict): ...
```

[▲ Back to top](#-table-of-contents)

---

### `dict_max_length`

Validated type for a dictionary with a maximum number of items.

**Init Params:**
* `max_length` (*int*): The maximum number of key-value pairs the dictionary may
  contain (inclusive).

**Validation pipeline:**
1. Value must be of type `dict`.
2. Value's length must be less than or equal to `max_length`.

**Example usage:**
```python
SmallDict = dict_max_length(10)

@validate_call
def process(data: SmallDict): ...
```

[▲ Back to top](#-table-of-contents)

---

### `list_not_empty`

Validated type for a non-empty list.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `list`.
2. Value must not be empty (must contain at least one item).

**Example usage:**
```python
@validate_call
def process(items: list_not_empty): ...
```

[▲ Back to top](#-table-of-contents)

---

### `list_unique`

Validated type for a list whose items are all unique.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `list`.
2. All items in the list must be unique (no duplicates).

**Example usage:**
```python
@validate_call
def process(items: list_unique): ...
```

[▲ Back to top](#-table-of-contents)

---

### `list_unique_not_empty`

Validated type for a non-empty list whose items are all unique.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `list`.
2. Value must not be empty (must contain at least one item).
3. All items in the list must be unique (no duplicates).

**Example usage:**
```python
@validate_call
def process(items: list_unique_not_empty): ...
```

[▲ Back to top](#-table-of-contents)

---

### `list_of`

Validated type for a list whose every item satisfies a given rule.

**Init Params:**
* `item_rule` (*Rule | Callable[[Any], bool]*): Rule that every single item of the
  list must satisfy.

**Validation pipeline:**
1. Value must be of type `list`.
2. Every item of the list must satisfy `item_rule`.

**Detailed description:**
`item_rule` is applied to each item individually (see `for_each`) — if validation
fails for a single item, validation of the whole list fails. `item_rule` itself may
be an arbitrarily composed rule (e.g. via `&`, `|`, `~`), including another
`validated type` used as a nested annotation.

**Example usage:**
```python
PositiveIntList = list_of(greater_than(0))

@validate_call
def register(scores: PositiveIntList): ...
```

[▲ Back to top](#-table-of-contents)

---

### `list_length`

Validated type for a list with an exact number of items.

**Init Params:**
* `exact` (*int*): The exact number of items the list must contain.

**Validation pipeline:**
1. Value must be of type `list`.
2. Value's length must equal `exact`.

**Example usage:**
```python
TripletList = list_length(3)

@validate_call
def process(items: TripletList): ...
```

[▲ Back to top](#-table-of-contents)

---

### `list_min_length`

Validated type for a list with a minimum number of items.

**Init Params:**
* `min_length` (*int*): The minimum number of items the list must contain
  (inclusive).

**Validation pipeline:**
1. Value must be of type `list`.
2. Value's length must be greater than or equal to `min_length`.

**Example usage:**
```python
NonTrivialList = list_min_length(2)

@validate_call
def process(items: NonTrivialList): ...
```

[▲ Back to top](#-table-of-contents)

---

### `list_max_length`

Validated type for a list with a maximum number of items.

**Init Params:**
* `max_length` (*int*): The maximum number of items the list may contain
  (inclusive).

**Validation pipeline:**
1. Value must be of type `list`.
2. Value's length must be less than or equal to `max_length`.

**Example usage:**
```python
SmallList = list_max_length(10)

@validate_call
def process(items: SmallList): ...
```

[▲ Back to top](#-table-of-contents)

---

### `set_not_empty`

Validated type for a non-empty set.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `set`.
2. Value must not be empty (must contain at least one item).

**Example usage:**
```python
@validate_call
def process(items: set_not_empty): ...
```

[▲ Back to top](#-table-of-contents)

---

### `set_of`

Validated type for a set whose every item satisfies a given rule.

**Init Params:**
* `item_rule` (*Rule | Callable[[Any], bool]*): Rule that every single item of the
  set must satisfy.

**Validation pipeline:**
1. Value must be of type `set`.
2. Every item of the set must satisfy `item_rule`.

**Detailed description:**
`item_rule` is applied to each item individually (see `for_each`) — if validation
fails for a single item, validation of the whole set fails. `item_rule` itself may
be an arbitrarily composed rule (e.g. via `&`, `|`, `~`), including another
`validated type` used as a nested annotation. Note that, unlike `list`/`tuple`, set
items have no defined order.

**Example usage:**
```python
PositiveIntSet = set_of(greater_than(0))

@validate_call
def register(scores: PositiveIntSet): ...
```

[▲ Back to top](#-table-of-contents)

---

### `set_length`

Validated type for a set with an exact number of items.

**Init Params:**
* `exact` (*int*): The exact number of items the set must contain.

**Validation pipeline:**
1. Value must be of type `set`.
2. Value's length must equal `exact`.

**Example usage:**
```python
TripletSet = set_length(3)

@validate_call
def process(items: TripletSet): ...
```

[▲ Back to top](#-table-of-contents)

---

### `set_min_length`

Validated type for a set with a minimum number of items.

**Init Params:**
* `min_length` (*int*): The minimum number of items the set must contain
  (inclusive).

**Validation pipeline:**
1. Value must be of type `set`.
2. Value's length must be greater than or equal to `min_length`.

**Example usage:**
```python
NonTrivialSet = set_min_length(2)

@validate_call
def process(items: NonTrivialSet): ...
```

[▲ Back to top](#-table-of-contents)

---

### `set_max_length`

Validated type for a set with a maximum number of items.

**Init Params:**
* `max_length` (*int*): The maximum number of items the set may contain
  (inclusive).

**Validation pipeline:**
1. Value must be of type `set`.
2. Value's length must be less than or equal to `max_length`.

**Example usage:**
```python
SmallSet = set_max_length(10)

@validate_call
def process(items: SmallSet): ...
```

[▲ Back to top](#-table-of-contents)

---

### `tuple_not_empty`

Validated type for a non-empty tuple.

**Init Params:**
*(no parameters)*

**Validation pipeline:**
1. Value must be of type `tuple`.
2. Value must not be empty (must contain at least one item).

**Example usage:**
```python
@validate_call
def process(items: tuple_not_empty): ...
```

[▲ Back to top](#-table-of-contents)

---

### `tuple_of`

Validated type for a tuple whose every item satisfies a given rule.

**Init Params:**
* `item_rule` (*Rule | Callable[[Any], bool]*): Rule that every single item of the
  tuple must satisfy.

**Validation pipeline:**
1. Value must be of type `tuple`.
2. Every item of the tuple must satisfy `item_rule`.

**Detailed description:**
`item_rule` is applied to each item individually (see `for_each`) — if validation
fails for a single item, validation of the whole tuple fails. `item_rule` itself may
be an arbitrarily composed rule (e.g. via `&`, `|`, `~`), including another
`validated type` used as a nested annotation. This applies `item_rule` uniformly to
every position; it does not validate fixed-position tuples of mixed types (e.g.
`tuple[int, str]`) element-by-element.

**Example usage:**
```python
PositiveIntTuple = tuple_of(greater_than(0))

@validate_call
def register(scores: PositiveIntTuple): ...
```

[▲ Back to top](#-table-of-contents)

---

### `tuple_length`

Validated type for a tuple with an exact number of items.

**Init Params:**
* `exact` (*int*): The exact number of items the tuple must contain.

**Validation pipeline:**
1. Value must be of type `tuple`.
2. Value's length must equal `exact`.

**Example usage:**
```python
TripletTuple = tuple_length(3)

@validate_call
def process(items: TripletTuple): ...
```

[▲ Back to top](#-table-of-contents)

---

### `tuple_min_length`

Validated type for a tuple with a minimum number of items.

**Init Params:**
* `min_length` (*int*): The minimum number of items the tuple must contain
  (inclusive).

**Validation pipeline:**
1. Value must be of type `tuple`.
2. Value's length must be greater than or equal to `min_length`.

**Example usage:**
```python
NonTrivialTuple = tuple_min_length(2)

@validate_call
def process(items: NonTrivialTuple): ...
```

[▲ Back to top](#-table-of-contents)

---

### `tuple_max_length`

Validated type for a tuple with a maximum number of items.

**Init Params:**
* `max_length` (*int*): The maximum number of items the tuple may contain
  (inclusive).

**Validation pipeline:**
1. Value must be of type `tuple`.
2. Value's length must be less than or equal to `max_length`.

**Example usage:**
```python
SmallTuple = tuple_max_length(10)

@validate_call
def process(items: SmallTuple): ...
```

[▲ Back to top](#-table-of-contents)

---

[⬅️ Back to main README](README_TYPES.md)