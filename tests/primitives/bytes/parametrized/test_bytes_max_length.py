"""Tests for bytes_max_length parametrized validated type."""

import pytest
from simplibs.types.primitives.bytes.parametrized.bytes_max_length import bytes_max_length
from simplibs.validate.testing import assert_type_contract


def test_bytes_max_length_contract(subtests: pytest.Item) -> None:
    """Verify that bytes_max_length satisfies full type contract & @validate_call integration."""
    max_two_bytes = bytes_max_length(2)

    assert_type_contract(
        subtests,
        type_=max_two_bytes,
        valid_values=[
            b"",           # Length 0 <= 2
            b"a",          # Length 1 <= 2
            b"ab",         # Length 2 <= 2
        ],
        invalid_values=[
            b"abc",        # Length 3 > 2
        ],
        expected_error_name="HAS_LENGTH_ERROR",
    )