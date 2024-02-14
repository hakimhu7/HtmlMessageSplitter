import unittest
from split import split_html_message

class TestSplitHtmlMessage(unittest.TestCase):

    def test_large_content(self):
        # Test with large HTML content
        html_content = "<p>" + "a" * 10000 + "</p>"
        fragments = list(split_html_message(html_content))
        self.assertEqual(len(fragments), 2)  # Expected to be split into 2 fragments

    def test_with_different_block_tags(self):
        # Test with HTML content containing various block tags
        html_content = "<div><p>This is a <b>test</b> message.</p><ul><li>Item 1</li><li>Item 2</li></ul></div>"
        fragments = list(split_html_message(html_content))
        self.assertEqual(len(fragments), 1)  # Expected to be split into 1 fragment

    def test_with_nested_tags(self):
        # Test with HTML content containing nested block tags
        html_content = "<div><p>This is a <b>test</b> message.</p><div><p>Nested paragraph.</p></div></div>"
        fragments = list(split_html_message(html_content))
        self.assertEqual(len(fragments), 1)  # Expected to be split into 1 fragment


if __name__ == "__main__":
    unittest.main()
