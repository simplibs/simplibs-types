"""Tests for int_uint8 validated type."""

import pytest
from simplibs.types.primitives.int.direct.int_uint8 import int_uint8
from simplibs.validate.testing import assert_type_contract


def test_int_uint8_contract(subtests: pytest.Item) -> None:
    """Verify that int_uint8 satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=int_uint8,
        valid_values=[
            0,
            128,
            255,
        ],
        invalid_values=[
            -1,
            256,
        ],
        expected_error_name="IN_RANGE_ERROR",
    )