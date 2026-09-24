"""Tests for int_day_of_month validated type."""

import pytest
from simplibs.types.primitives.int.direct.int_day_of_month import int_day_of_month
from simplibs.validate.testing import assert_type_contract


def test_int_day_of_month_contract(subtests: pytest.Item) -> None:
    """Verify that int_day_of_month satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=int_day_of_month,
        valid_values=[
            1,
            15,
            31,
        ],
        invalid_values=[
            0,
            32,
            -1,
        ],
        expected_error_name="IN_RANGE_ERROR",
    )