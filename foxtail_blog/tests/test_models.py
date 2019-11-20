from django.test import TestCase
from django.urls import reverse

from foxtail_blog.models import Post


class PostModelTest(TestCase):
    def test_string_representation(self):
        post = Post(title="title-1")
        self.assertEqual(str(post), post.title)

    def test_absolute_url(self):
        post = Post(title="title-1", slug="slug-1")
        correct_url = reverse('blog_detail', kwargs={'slug': 'slug-1'})
        self.assertEqual(post.get_absolute_url(), correct_url)
