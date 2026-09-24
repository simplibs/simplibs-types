"""Tests for bytes_not_empty validated type."""

import pytest
from simplibs.types.primitives.bytes.direct.bytes_not_empty import bytes_not_empty
from simplibs.validate.testing import assert_type_contract


def test_bytes_not_empty_contract(subtests: pytest.Item) -> None:
    """Verify that bytes_not_empty satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=bytes_not_empty,
        valid_values=[
            b"a",
            b"hello",
            bytes([1, 2, 3]),
        ],
        invalid_values=[
            b"",
            bytes(),
        ],
        expected_error_name="NOT_EMPTY_ERROR",
    )