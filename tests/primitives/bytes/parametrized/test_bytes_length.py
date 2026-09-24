"""Tests for bytes_length parametrized validated type."""

import pytest
from simplibs.types.primitives.bytes.parametrized.bytes_length import bytes_length
from simplibs.validate.testing import assert_type_contract


def test_bytes_length_contract(subtests: pytest.Item) -> None:
    """Verify that bytes_length satisfies full type contract & @validate_call integration."""
    two_bytes = bytes_length(2)

    assert_type_contract(
        subtests,
        type_=two_bytes,
        valid_values=[
            b"ab",
            b"\x00\x01",
        ],
        invalid_values=[
            b"",           # Length 0 != 2
            b"a",          # Length 1 != 2
            b"abc",        # Length 3 != 2
        ],
        expected_error_name="HAS_LENGTH_ERROR",
    )