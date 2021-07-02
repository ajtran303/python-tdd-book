from django.test import TestCase


class HomePageTest(TestCase):

    def test_home_page(self):
        # Django has shortcuts instead of using selenium
        response = self.client.get('/')
        self.assertIn(
            '<title>To-Do</title>',
            response.content.decode()
        )
        self.assertTrue(response.content.decode().startswith('<html>'))
        self.assertTrue(response.content.decode().strip().endswith('</html>'))
