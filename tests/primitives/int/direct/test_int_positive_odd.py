"""Tests for int_positive_odd validated type."""

import pytest
from simplibs.types.primitives.int.direct.int_positive_odd import int_positive_odd
from simplibs.validate.testing import assert_type_contract


def test_int_positive_odd_contract(subtests: pytest.Item) -> None:
    """Verify that int_positive_odd satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=int_positive_odd,
        valid_values=[
            1,
            3,
            99,
        ],
        invalid_values=[
            0,   # Fails on GREATER_THAN
            -1,  # Fails on GREATER_THAN
            2,   # Fails on IS_ODD
        ],
        expected_error_name=[
            "GREATER_THAN_ERROR",
            "GREATER_THAN_ERROR",
            "IS_ODD_ERROR",
        ],
    )