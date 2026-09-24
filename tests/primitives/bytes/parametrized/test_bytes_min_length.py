"""Tests for bytes_min_length parametrized validated type."""

import pytest
from simplibs.types.primitives.bytes.parametrized.bytes_min_length import bytes_min_length
from simplibs.validate.testing import assert_type_contract


def test_bytes_min_length_contract(subtests: pytest.Item) -> None:
    """Verify that bytes_min_length satisfies full type contract & @validate_call integration."""
    min_two_bytes = bytes_min_length(2)

    assert_type_contract(
        subtests,
        type_=min_two_bytes,
        valid_values=[
            b"ab",         # Length 2 >= 2
            b"abc",        # Length 3 >= 2
        ],
        invalid_values=[
            b"",           # Length 0 < 2
            b"a",          # Length 1 < 2
        ],
        expected_error_name="HAS_LENGTH_ERROR",
    )