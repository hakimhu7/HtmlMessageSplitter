import unittest
from split import split_html_message

class TestSplitHtmlMessage(unittest.TestCase):

    def test_large_content(self):
        # Test with large HTML content
        html_content = "<p>" + "a" * 10000 + "</p>"
        fragments = list(split_html_message(html_content))
        self.assertEqual(len(fragments), 3)  # Expected to be split into 3 fragments

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

    def test_with_different_max_len_values(self):
        # Test with different max_len values
        html_content = "<p>This is a <b>test</b> message.</p>"
        fragments_100 = list(split_html_message(html_content, max_len=100))
        fragments_1000 = list(split_html_message(html_content, max_len=1000))
        fragments_5000 = list(split_html_message(html_content, max_len=5000))
        self.assertEqual(len(fragments_100), 2)  # Expected to be split into 2 fragments
        self.assertEqual(len(fragments_1000), 1)  # Expected to be split into 1 fragment
        self.assertEqual(len(fragments_5000), 1)  # Expected to be split into 1 fragment

    def test_with_empty_input(self):
        # Test with empty HTML content
        html_content = ""
        fragments = list(split_html_message(html_content))
        self.assertEqual(fragments, [])  # Expected empty list

    def test_with_html_content_without_block_tags(self):
        # Test with HTML content without block tags
        html_content = "This is a plain text message."
        fragments = list(split_html_message(html_content))
        self.assertEqual(fragments, ['This is a plain text message.'])  # Expected single fragment

    def test_with_special_characters(self):
        # Test with HTML content containing special characters
        html_content = "<p>This is <b>special</b> &amp; important.</p>"
        fragments = list(split_html_message(html_content))
        self.assertEqual(len(fragments), 1)  # Expected single fragment

    def test_with_invalid_html_content(self):
        # Test with invalid HTML content
        html_content = "<p>This is a <b>test message.</p>"  # Missing closing </b> tag
        fragments = list(split_html_message(html_content))
        self.assertEqual(len(fragments), 1)  # Expected single fragment

if __name__ == "__main__":
    unittest.main()
