"""Tests for int_month validated type."""

import pytest
from simplibs.types.primitives.int.direct.int_month import int_month
from simplibs.validate.testing import assert_type_contract


def test_int_month_contract(subtests: pytest.Item) -> None:
    """Verify that int_month satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=int_month,
        valid_values=[
            1,
            6,
            12,
        ],
        invalid_values=[
            0,
            13,
            -1,
        ],
        expected_error_name="IN_RANGE_ERROR",
    )