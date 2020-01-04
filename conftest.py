from django.test import RequestFactory

import pytest
from published.constants import NEVER_AVAILABLE
from pytest_factoryboy import register

from foxtail_blog.tests.factories import PostFactory

register(PostFactory, "post")
register(PostFactory, "second_post")
register(PostFactory, "hidden_post", publish_status=NEVER_AVAILABLE)


@pytest.fixture
def request_factory() -> RequestFactory:
    return RequestFactory()
