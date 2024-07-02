from django.test import TestCase
from django.urls import reverse
from .forms import CommentForm
from .models import C

class TestBlogViews(TestCase):

    def setUp(self):
        """Create a superuser and a blog post"""
        self.user = User.objects.create_superuser(
            username="myUsername", password="myPassword", email="test@test.com")
        self.post = Post.objects.create(
            title="Blog title", author=self.user,
            slug="blog-title", excerpt="Blog excerpt",
            content="Blog content", status=1)

    def test_render_post_detail_page_with_comment_form(self):
        """Verifies a single blog post containing a comment form is returned"""
        response = self.client.get(reverse('post_detail', args=['blog-title']))

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Blog title", response.content)
        self.assertIn(b"Blog content", response.content)
        self.assertIsInstance(response.context['comment_form'], CommentForm)


