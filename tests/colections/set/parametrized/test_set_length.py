"""Tests for set_length parametrized validated type."""

import pytest
from simplibs.types.collections.set.parametrized.set_length import set_length
from simplibs.validate.testing import assert_type_contract


def test_set_length_contract(subtests: pytest.Item) -> None:
    """Verify that set_length satisfies full type contract & @validate_call integration."""
    two_item_set = set_length(2)

    assert_type_contract(
        subtests,
        type_=two_item_set,
        valid_values=[
            {1, 2},
            {"a", "b"},
        ],
        invalid_values=[
            set(),           # Length 0 != 2
            {1},             # Length 1 != 2
            {1, 2, 3},       # Length 3 != 2
        ],
        expected_error_name="HAS_LENGTH_ERROR",
    )