# Direct:
from .direct.bytes_empty import bytes_empty
from .direct.bytes_not_empty import bytes_not_empty
# Parametric:
from .parametrized.bytes_length import bytes_length
from .parametrized.bytes_min_length import bytes_min_length
from .parametrized.bytes_max_length import bytes_max_length
from .parametrized.bytes_length_range import bytes_length_range


_DESIGN_NOTES = """
# Bytes Presets Sub-Package

## Purpose
Validated types for `bytes` — emptiness and length constraints (exact,
minimum, maximum, and range).

## Internal Components Registry

| Component              | Type            | Description                                       |
| :----------------------- | :-------------- | :--------------------------------------------------- |
| `bytes_empty`            | Validated Type  | Empty bytes.                                          |
| `bytes_not_empty`        | Validated Type  | Non-empty bytes.                                      |
| `bytes_length`           | Factory         | Bytes with an exact length.                           |
| `bytes_min_length`       | Factory         | Bytes with a minimum length.                          |
| `bytes_max_length`       | Factory         | Bytes with a maximum length.                          |
| `bytes_length_range`     | Factory         | Bytes with a length in an inclusive range.            |
"""