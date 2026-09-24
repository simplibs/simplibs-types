"""Tests for int_year validated type."""

import pytest
from simplibs.types.primitives.int.direct.int_year import int_year
from simplibs.validate.testing import assert_type_contract


def test_int_year_contract(subtests: pytest.Item) -> None:
    """Verify that int_year satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=int_year,
        valid_values=[
            1,
            2026,
            9999,
        ],
        invalid_values=[
            0,
            10000,
            -1,
        ],
        expected_error_name="IN_RANGE_ERROR",
    )