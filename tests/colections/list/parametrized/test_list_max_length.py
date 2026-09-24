"""Tests for list_max_length parametrized validated type."""

import pytest
from simplibs.types.collections.list.parametrized.list_max_length import list_max_length
from simplibs.validate.testing import assert_type_contract


def test_list_max_length_contract(subtests: pytest.Item) -> None:
    """Verify that list_max_length satisfies full type contract & @validate_call integration."""
    max_two_list = list_max_length(2)

    assert_type_contract(
        subtests,
        type_=max_two_list,
        valid_values=[
            [],             # Length 0 <= 2
            [1],            # Length 1 <= 2
            [1, 2],         # Length 2 <= 2
        ],
        invalid_values=[
            [1, 2, 3],      # Length 3 > 2
        ],
        expected_error_name="HAS_LENGTH_ERROR",
    )