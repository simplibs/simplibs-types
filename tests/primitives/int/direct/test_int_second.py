"""Tests for int_second validated type."""

import pytest
from simplibs.types.primitives.int.direct.int_second import int_second
from simplibs.validate.testing import assert_type_contract


def test_int_second_contract(subtests: pytest.Item) -> None:
    """Verify that int_second satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=int_second,
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