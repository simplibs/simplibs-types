"""Tests for int_non_negative_even validated type."""

import pytest
from simplibs.types.primitives.int.direct.int_non_negative_even import int_non_negative_even
from simplibs.validate.testing import assert_type_contract


def test_int_non_negative_even_contract(subtests: pytest.Item) -> None:
    """Verify that int_non_negative_even satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=int_non_negative_even,
        valid_values=[
            0,
            2,
            100,
        ],
        invalid_values=[
            -2,  # Fails on GREATER_OR_EQUAL
            1,   # Fails on IS_EVEN
        ],
        expected_error_name=[
            "GREATER_OR_EQUAL_ERROR",
            "IS_EVEN_ERROR",
        ],
    )