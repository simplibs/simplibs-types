"""Tests for dict_max_length parametrized validated type."""

import pytest
from simplibs.types.collections.dict.parametrized.dict_max_length import dict_max_length
from simplibs.validate.testing import assert_type_contract


def test_dict_max_length_contract(subtests: pytest.Item) -> None:
    """Verify that dict_max_length satisfies full type contract & @validate_call integration."""
    max_two_dict = dict_max_length(2)

    assert_type_contract(
        subtests,
        type_=max_two_dict,
        valid_values=[
            {},                   # Length 0 <= 2
            {"a": 1},             # Length 1 <= 2
            {"a": 1, "b": 2},     # Length 2 <= 2
        ],
        invalid_values=[
            {"a": 1, "b": 2, "c": 3},  # Length 3 > 2
        ],
        expected_error_name="HAS_LENGTH_ERROR",
    )