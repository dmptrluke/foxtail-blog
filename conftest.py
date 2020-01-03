from django.test import RequestFactory

import pytest
from pytest_factoryboy import register

from foxtail_blog.tests.factories import PostFactory

register(PostFactory, "post")
register(PostFactory, "second_post")


@pytest.fixture
def request_factory() -> RequestFactory:
    return RequestFactory()
