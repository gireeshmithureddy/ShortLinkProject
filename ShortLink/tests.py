from django.test import TestCase
import requests
from .models import ShortLink

# Create your tests here.

class MyViewTestCase(TestCase):
    def setUp(self):
        # Set up any necessary data for your tests here
        #self.test_model = ShortLink.objects.create(name="Test Name")
        pass

    def test_shortUrl_Gen(self):
        data = {"long_url": "https://www.appsloveworld.com/django/100/32/typeerror-at-admin-set-object-is-not-reversible-and-argument-to-reverse-mu"}

        response = requests.post("http://localhost:8000/api/v1/shortlinks/", data=data)

        self.assertEqual(response.status_code, 201)

        #self.assertIn("Test Name", response.text)