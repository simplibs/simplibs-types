"""Tests for dict_length parametrized validated type."""

import pytest
from simplibs.types.collections.dict.parametrized.dict_length import dict_length
from simplibs.validate.testing import assert_type_contract


def test_dict_length_contract(subtests: pytest.Item) -> None:
    """Verify that dict_length satisfies full type contract & @validate_call integration."""
    # Vytvoříme konkrétní typ pro slovník se přesně 2 prvky
    two_item_dict = dict_length(2)

    assert_type_contract(
        subtests,
        type_=two_item_dict,
        valid_values=[
            {"a": 1, "b": 2},
            {1: "x", 2: "y"},
        ],
        invalid_values=[
            {},                   # Fails: length 0 != 2
            {"a": 1},             # Fails: length 1 != 2
            {"a": 1, "b": 2, "c": 3},  # Fails: length 3 != 2
        ],
        expected_error_name="HAS_LENGTH_ERROR",
    )