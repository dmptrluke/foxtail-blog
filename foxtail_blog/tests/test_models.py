import pytest

from ..models import Post

pytestmark = pytest.mark.django_db


def test_string_representation(post: Post):
    assert str(post) == post.title


def test_get_absolute_url(post: Post):
    assert post.get_absolute_url() == f"/blog/{post.slug}/"
