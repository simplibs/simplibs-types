"""Tests for bytes_length_range parametrized validated type."""

import pytest
from simplibs.types.primitives.bytes.parametrized.bytes_length_range import bytes_length_range
from simplibs.validate.testing import assert_type_contract


def test_bytes_length_range_contract(subtests: pytest.Item) -> None:
    """Verify that bytes_length_range satisfies full type contract & @validate_call integration."""
    range_bytes = bytes_length_range(2, 4)

    assert_type_contract(
        subtests,
        type_=range_bytes,
        valid_values=[
            b"ab",         # Length 2 (inclusive min)
            b"abc",        # Length 3
            b"abcd",       # Length 4 (inclusive max)
        ],
        invalid_values=[
            b"",           # Length 0 < 2
            b"a",          # Length 1 < 2
            b"abcde",      # Length 5 > 4
        ],
        expected_error_name="HAS_LENGTH_ERROR",
    )