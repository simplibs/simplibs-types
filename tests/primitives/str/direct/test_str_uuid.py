"""Tests for str_uuid validated type."""

import pytest
from simplibs.types.primitives.str.direct.str_uuid import str_uuid
from simplibs.validate.testing import assert_type_contract


def test_str_uuid_contract(subtests: pytest.Item) -> None:
    """Verify that str_uuid satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=str_uuid,
        valid_values=[
            "123e4567-e89b-12d3-a456-426614174000",
            "123E4567-E89B-12D3-A456-426614174000",
            "00000000-0000-0000-0000-000000000000",
        ],
        invalid_values=[
            "",
            "123e4567e89b12d3a456426614174000",
            "123e4567-e89b-12d3-a456-4266141740000",
            "123e4567-e89b-12d3-a456-42661417400g",
        ],
        expected_error_name="REGEX_ERROR",
    )