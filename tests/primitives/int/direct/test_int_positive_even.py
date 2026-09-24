"""Tests for int_positive_even validated type."""

import pytest
from simplibs.types.primitives.int.direct.int_positive_even import int_positive_even
from simplibs.validate.testing import assert_type_contract


def test_int_positive_even_contract(subtests: pytest.Item) -> None:
    """Verify that int_positive_even satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=int_positive_even,
        valid_values=[
            2,
            4,
            100,
        ],
        invalid_values=[
            0,   # Fails on GREATER_THAN
            -2,  # Fails on GREATER_THAN
            1,   # Fails on IS_EVEN
        ],
        expected_error_name=[
            "GREATER_THAN_ERROR",
            "GREATER_THAN_ERROR",
            "IS_EVEN_ERROR",
        ],
    )