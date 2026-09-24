"""Tests for int_odd validated type."""

import pytest
from simplibs.types.primitives.int.direct.int_odd import int_odd
from simplibs.validate.testing import assert_type_contract


def test_int_odd_contract(subtests: pytest.Item) -> None:
    """Verify that int_odd satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=int_odd,
        valid_values=[
            1,
            -1,
            3,
            -3,
            99,
        ],
        invalid_values=[
            0,
            2,
            -2,
            100,
        ],
        expected_error_name="IS_ODD_ERROR",
    )