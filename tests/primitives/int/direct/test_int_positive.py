"""Tests for int_positive validated type."""

import pytest
from simplibs.types.primitives.int.direct.int_positive import int_positive
from simplibs.validate.testing import assert_type_contract


def test_int_positive_contract(subtests: pytest.Item) -> None:
    """Verify that int_positive satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=int_positive,
        valid_values=[
            1,
            10,
            1000,
        ],
        invalid_values=[
            0,
            -1,
            -10,
        ],
        expected_error_name="GREATER_THAN_ERROR",
    )