"""Tests for int_negative validated type."""

import pytest
from simplibs.types.primitives.int.direct.int_negative import int_negative
from simplibs.validate.testing import assert_type_contract


def test_int_negative_contract(subtests: pytest.Item) -> None:
    """Verify that int_negative satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=int_negative,
        valid_values=[
            -1,
            -10,
            -1000,
        ],
        invalid_values=[
            0,
            1,
            100,
        ],
        expected_error_name="LESS_THAN_ERROR",
    )