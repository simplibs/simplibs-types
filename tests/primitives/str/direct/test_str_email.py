"""Tests for str_email validated type."""

import pytest
from simplibs.types.primitives.str.direct.str_email import str_email
from simplibs.validate.testing import assert_type_contract


def test_str_email_contract(subtests: pytest.Item) -> None:
    """Verify that str_email satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=str_email,
        valid_values=[
            "user@example.com",
            "john.doe@sub.domain.org",
            "a@b.cz",
        ],
        invalid_values=[
            "",
            "invalid.email",
            "@domain.com",
            "user@",
            "user@domain",
            "user name@domain.com",
        ],
        expected_error_name="REGEX_ERROR",
    )