"""Tests for int_minute validated type."""

import pytest
from simplibs.types.primitives.int.direct.int_minute import int_minute
from simplibs.validate.testing import assert_type_contract


def test_int_minute_contract(subtests: pytest.Item) -> None:
    """Verify that int_minute satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=int_minute,
        valid_values=[
            0,
            30,
            59,
        ],
        invalid_values=[
            -1,
            60,
        ],
        expected_error_name="IN_RANGE_ERROR",
    )