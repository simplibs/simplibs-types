"""Tests for str_snake_case validated type."""

import pytest
from simplibs.types.primitives.str.direct.str_snake_case import str_snake_case
from simplibs.validate.testing import assert_type_contract


def test_str_snake_case_contract(subtests: pytest.Item) -> None:
    """Verify that str_snake_case satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=str_snake_case,
        valid_values=[
            "my_variable_name",
            "var",
            "variable_123",
        ],
        invalid_values=[
            "",
            "123_variable",
            "_my_variable",
            "my_variable_",
            "my__variable",
            "MyVariable",
            "my-variable",
        ],
        expected_error_name="REGEX_ERROR",
    )