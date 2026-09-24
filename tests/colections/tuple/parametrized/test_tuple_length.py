"""Tests for tuple_length parametrized validated type."""

import pytest
from simplibs.types.collections.tuple.parametrized.tuple_length import tuple_length
from simplibs.validate.testing import assert_type_contract


def test_tuple_length_contract(subtests: pytest.Item) -> None:
    """Verify that tuple_length satisfies full type contract & @validate_call integration."""
    two_item_tuple = tuple_length(2)

    assert_type_contract(
        subtests,
        type_=two_item_tuple,
        valid_values=[
            (1, 2),
            ("a", "b"),
        ],
        invalid_values=[
            (),             # Length 0 != 2
            (1,),           # Length 1 != 2
            (1, 2, 3),      # Length 3 != 2
        ],
        expected_error_name="HAS_LENGTH_ERROR",
    )