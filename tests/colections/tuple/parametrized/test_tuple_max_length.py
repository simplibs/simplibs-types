"""Tests for tuple_max_length parametrized validated type."""

import pytest
from simplibs.types.collections.tuple.parametrized.tuple_max_length import tuple_max_length
from simplibs.validate.testing import assert_type_contract


def test_tuple_max_length_contract(subtests: pytest.Item) -> None:
    """Verify that tuple_max_length satisfies full type contract & @validate_call integration."""
    max_two_tuple = tuple_max_length(2)

    assert_type_contract(
        subtests,
        type_=max_two_tuple,
        valid_values=[
            (),             # Length 0 <= 2
            (1,),           # Length 1 <= 2
            (1, 2),         # Length 2 <= 2
        ],
        invalid_values=[
            (1, 2, 3),      # Length 3 > 2
        ],
        expected_error_name="HAS_LENGTH_ERROR",
    )