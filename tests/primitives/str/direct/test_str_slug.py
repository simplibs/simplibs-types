"""Tests for str_slug validated type."""

import pytest
from simplibs.types.primitives.str.direct.str_slug import str_slug
from simplibs.validate.testing import assert_type_contract


def test_str_slug_contract(subtests: pytest.Item) -> None:
    """Verify that str_slug satisfies full type contract & @validate_call integration."""
    assert_type_contract(
        subtests,
        type_=str_slug,
        valid_values=[
            "my-blog-post",
            "article-123",
            "simple",
        ],
        invalid_values=[
            "",
            "-my-blog-post",
            "my-blog-post-",
            "my--blog-post",
            "My-Blog-Post",
            "my_blog_post",
            "my blog post",
        ],
        expected_error_name="REGEX_ERROR",
    )