import unittest
from split import split_html_message
DEFAULT_MAX_LEN = 4396 #test_html_content_exceeding_max_length

class TestSplitHtmlMessage(unittest.TestCase):
    """
Test suite for the split_html_message function.

Methods:
test_large_content: Test with large HTML content.
test_with_different_block_tags: Test with various block tags in HTML content.
test_with_nested_tags: Test with nested block tags in HTML content.
test_empty_html_content: Test with empty HTML content.
test_html_content_exceeding_max_length: Test with HTML content exceeding maximum length.
test_html_content_with_inline_styling_and_attributes: Test with HTML content containing inline styling and attributes.
    """
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

    def test_empty_html_content(self):
    # Test with empty HTML content
        html_content = ""
        fragments = list(split_html_message(html_content))
        self.assertEqual(len(fragments), 0)  # Expected to produce no fragments

    def test_html_content_exceeding_max_length(self):
    # Test with HTML content exceeding maximum length
        html_content = "<p>" + "a" * (DEFAULT_MAX_LEN + 100) + "</p>"
        fragments = list(split_html_message(html_content))
        self.assertTrue(len(fragments) > 1)  # Expected to be split into multiple fragments

    def test_html_content_with_inline_styling_and_attributes(self):
    # Test with HTML content containing inline styling and attributes
        html_content = '<p style="color: red;">This is a <b>test</b> message.</p>'
        fragments = list(split_html_message(html_content))
        self.assertEqual(len(fragments), 1)  # Expected to be split into 1 fragment

if __name__ == "__main__":
    unittest.main()
