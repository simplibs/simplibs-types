"""Tests for int_in_range parametrized validated type."""

import pytest
from simplibs.types.primitives.int.parametrized.int_in_range import int_in_range
from simplibs.validate.testing import assert_type_contract


def test_int_in_range_contract(subtests: pytest.Item) -> None:
    """Verify that int_in_range satisfies full type contract & @validate_call integration."""
    score_range = int_in_range(0, 100)

    assert_type_contract(
        subtests,
        type_=score_range,
        valid_values=[
            0,         # Inclusive min
            50,
            100,       # Inclusive max
        ],
        invalid_values=[
            -1,        # Less than min
            101,       # Greater than max
        ],
        expected_error_name="IN_RANGE_ERROR",
    )