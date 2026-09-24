"""Tests for str_url validated type."""

import pytest
from simplibs.types.primitives.str.direct.str_url import str_url
from simplibs.validate.testing import assert_type_contract


def test_str_url_contract(subtests: pytest.Item) -> None:
    """Verify that str_url satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=str_url,
        valid_values=[
            "http://example.com",
            "https://example.com/path?query=1#hash",
            "https://sub.domain.org/test",
        ],
        invalid_values=[
            "",
            "ftp://example.com",
            "example.com",
            "https://example .com",
            "http://",
        ],
        expected_error_name="REGEX_ERROR",
    )