"""Tests for set_min_length parametrized validated type."""

import pytest
from simplibs.types.collections.set.parametrized.set_min_length import set_min_length
from simplibs.validate.testing import assert_type_contract


def test_set_min_length_contract(subtests: pytest.Item) -> None:
    """Verify that set_min_length satisfies full type contract & @validate_call integration."""
    min_two_set = set_min_length(2)

    assert_type_contract(
        subtests,
        type_=min_two_set,
        valid_values=[
            {1, 2},          # Length 2 >= 2
            {1, 2, 3},       # Length 3 >= 2
        ],
        invalid_values=[
            set(),           # Length 0 < 2
            {1},             # Length 1 < 2
        ],
        expected_error_name="HAS_LENGTH_ERROR",
    )