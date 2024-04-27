from django.test import TestCase
from django.urls import reverse
from .models import Post
# Create your tests here.
class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(title='Test Title', content='Test Content')
    def test_test_content(self):
        post = Post.objects.get(id = 1)
        expected_object_title = f'{post.title}'
        expected_object_text = f'{post.text}'
        self.assertEqual(expected_object_title,'Test Title')
        self.assertEqual(expected_object_text,'Test Content')
class HomePageTests(TestCase):
    def setUp(self):
        Post.objects.create(title='Test Title', content='Test')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
    def test_view_url_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')