"""Tests for dict_not_empty validated type."""

import pytest
from simplibs.types.collections.dict.direct.dict_not_empty import dict_not_empty
from simplibs.validate.testing import assert_type_contract


def test_dict_not_empty_contract(subtests: pytest.Item) -> None:
    """Verify that dict_not_empty satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=dict_not_empty,
        valid_values=[
            {"a": 1},
            {"key": "value", "number": 42},
            {1: True},
        ],
        invalid_values=[
            {},  # Pouze hodnoty, které vyhodí NOT_EMPTY_ERROR
        ],
        expected_error_name="NOT_EMPTY_ERROR",
    )