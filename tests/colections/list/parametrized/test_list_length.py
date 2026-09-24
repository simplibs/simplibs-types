"""Tests for list_length parametrized validated type."""

import pytest
from simplibs.types.collections.list.parametrized.list_length import list_length
from simplibs.validate.testing import assert_type_contract


def test_list_length_contract(subtests: pytest.Item) -> None:
    """Verify that list_length satisfies full type contract & @validate_call integration."""
    two_item_list = list_length(2)

    assert_type_contract(
        subtests,
        type_=two_item_list,
        valid_values=[
            [1, 2],
            ["a", "b"],
        ],
        invalid_values=[
            [],             # Length 0 != 2
            [1],            # Length 1 != 2
            [1, 2, 3],      # Length 3 != 2
        ],
        expected_error_name="HAS_LENGTH_ERROR",
    )