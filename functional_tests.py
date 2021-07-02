import unittest
from selenium import webdriver


class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        # User visits site
        self.browser.get('http://localhost:8000')

        # Title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header = self.browser.find_element_by_tag_name('h1')
        self.assertIn('To-Do', header.text)

        # User can input text into a text box
        # User can press enter to update page with new to-do item
        # There is still a text box to input more text
        # User can enter another item


if __name__ == '__main__':
    unittest.main()
