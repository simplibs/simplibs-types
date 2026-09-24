"""Tests for int_non_negative validated type."""

import pytest
from simplibs.types.primitives.int.direct.int_non_negative import int_non_negative
from simplibs.validate.testing import assert_type_contract


def test_int_non_negative_contract(subtests: pytest.Item) -> None:
    """Verify that int_non_negative satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=int_non_negative,
        valid_values=[
            0,
            1,
            100,
        ],
        invalid_values=[
            -1,
            -10,
            -100,
        ],
        expected_error_name="GREATER_OR_EQUAL_ERROR",
    )