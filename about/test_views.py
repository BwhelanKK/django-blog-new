from django.test import TestCase
from django.urls import reverse
from .models import About
from .forms import CollaborateForm

class TestAboutViews(TestCase):

    def setUp(self):
        """Creates About Me content"""
        self.about_content = About(
            title="About Me", content="This is about me.")
        self.about_content.save()

        def test_render_about_page_with_collaborate_form(self):
            """Verifies a request for about me containing a collaboration form"""
            response = self.client.get(reverse('about'))
            self.assertEqual(response.status_code, 200)
            self.assertIn("About Me", response.content)
            self.assertIsInstance(response.context ['collaborate_form', CollaborateForm])
