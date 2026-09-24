"""Tests for set_max_length parametrized validated type."""

import pytest
from simplibs.types.collections.set.parametrized.set_max_length import set_max_length
from simplibs.validate.testing import assert_type_contract


def test_set_max_length_contract(subtests: pytest.Item) -> None:
    """Verify that set_max_length satisfies full type contract & @validate_call integration."""
    max_two_set = set_max_length(2)

    assert_type_contract(
        subtests,
        type_=max_two_set,
        valid_values=[
            set(),           # Length 0 <= 2
            {1},             # Length 1 <= 2
            {1, 2},          # Length 2 <= 2
        ],
        invalid_values=[
            {1, 2, 3},       # Length 3 > 2
        ],
        expected_error_name="HAS_LENGTH_ERROR",
    )