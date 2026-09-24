"""Tests for bytes_empty validated type."""

import pytest
from simplibs.types.primitives.bytes.direct.bytes_empty import bytes_empty
from simplibs.validate.testing import assert_type_contract


def test_bytes_empty_contract(subtests: pytest.Item) -> None:
    """Verify that bytes_empty satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=bytes_empty,
        valid_values=[
            b"",
            bytes(),
        ],
        invalid_values=[
            b"a",
            b"hello",
            bytes([1, 2, 3]),
        ],
        expected_error_name="IS_EMPTY_ERROR",
    )