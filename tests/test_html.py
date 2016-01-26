import unittest
from middleground.html import Html

class TestHtml(unittest.TestCase):
    def test_html_small(self):
        html = Html("<p>Hello, <a href='http://localhost/world'>world</a>!")
        htmlStr = str(html)
        self.assertEqual(htmlStr, "Hello, world!")

    def test_html_large(self):
        html = Html("<div><p>Hello, <a href='http://localhost/world'>world</a>!<br />Another.</div>")
        htmlStr = str(html)
        self.assertEqual(htmlStr, "Hello, world!  \nAnother.")

if __name__ == '__main__':
    unittest.main()
