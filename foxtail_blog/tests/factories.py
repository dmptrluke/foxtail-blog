from factory import DjangoModelFactory, Faker
from published.constants import AVAILABLE

from ..models import Post


class PostFactory(DjangoModelFactory):
    title = Faker('name')
    slug = Faker('slug')

    tags = f"{Faker('words')}, {Faker('words')}"

    allow_comments = True
    publish_status = AVAILABLE

    author = Faker('name')
    created = Faker('date_time_this_year')

    text = Faker('paragraph')

    class Meta:
        model = Post
