"""Tests for int_zero validated type."""

import pytest
from simplibs.types.primitives.int.direct.int_zero import int_zero
from simplibs.validate.testing import assert_type_contract


def test_int_zero_contract(subtests: pytest.Item) -> None:
    """Verify that int_zero satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=int_zero,
        valid_values=[
            0,
        ],
        invalid_values=[
            1,
            -1,
            100,
        ],
        expected_error_name="IS_ZERO_ERROR",
    )