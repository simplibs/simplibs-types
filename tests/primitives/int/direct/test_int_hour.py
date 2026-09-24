"""Tests for int_hour validated type."""

import pytest
from simplibs.types.primitives.int.direct.int_hour import int_hour
from simplibs.validate.testing import assert_type_contract


def test_int_hour_contract(subtests: pytest.Item) -> None:
    """Verify that int_hour satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=int_hour,
        valid_values=[
            0,
            12,
            23,
        ],
        invalid_values=[
            -1,
            24,
            100,
        ],
        expected_error_name="IN_RANGE_ERROR",
    )