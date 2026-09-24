"""Tests for int_non_positive validated type."""

import pytest
from simplibs.types.primitives.int.direct.int_non_positive import int_non_positive
from simplibs.validate.testing import assert_type_contract


def test_int_non_positive_contract(subtests: pytest.Item) -> None:
    """Verify that int_non_positive satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=int_non_positive,
        valid_values=[
            0,
            -1,
            -100,
        ],
        invalid_values=[
            1,
            10,
            100,
        ],
        expected_error_name="LESS_OR_EQUAL_ERROR",
    )