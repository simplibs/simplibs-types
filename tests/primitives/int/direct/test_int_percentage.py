"""Tests for int_percentage validated type."""

import pytest
from simplibs.types.primitives.int.direct.int_percentage import int_percentage
from simplibs.validate.testing import assert_type_contract


def test_int_percentage_contract(subtests: pytest.Item) -> None:
    """Verify that int_percentage satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=int_percentage,
        valid_values=[
            0,
            50,
            100,
        ],
        invalid_values=[
            -1,
            101,
            -50,
            150,
        ],
        expected_error_name="IN_RANGE_ERROR",
    )