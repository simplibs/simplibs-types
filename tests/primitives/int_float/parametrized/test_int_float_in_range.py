"""Tests for int_float_in_range parametrized validated type."""

import pytest
from simplibs.types.primitives.int_float.parametrized.int_float_in_range import int_float_in_range
from simplibs.validate.testing import assert_type_contract


def test_int_float_in_range_contract(subtests: pytest.Item) -> None:
    """Verify that int_float_in_range satisfies full type contract & @validate_call integration."""
    score_range = int_float_in_range(0, 100)

    assert_type_contract(
        subtests,
        type_=score_range,
        valid_values=[
            0,         # int min
            0.0,       # float min
            50,        # int middle
            50.5,      # float middle
            100,       # int max
            100.0,     # float max
        ],
        invalid_values=[
            -1,
            -0.1,
            101,
            100.1,
        ],
        expected_error_name="IN_RANGE_ERROR",
    )