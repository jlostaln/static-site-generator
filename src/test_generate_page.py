import unittest

from generate_page import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_valid_h1(self):
        self.assertEqual(extract_title("# Hello"), "Hello")
        self.assertEqual(extract_title("#    Trimmed Title   "), "Trimmed Title")

    def test_multiple_headers(self):
        md = "# First Title\n## Subtitle\n# Second Title"
        self.assertEqual(extract_title(md), "First Title") 

    def test_no_h1_header(self):
        md = "## Subtitle\n### Smaller heading\nJust text"
        with self.assertRaises(ValueError):
            extract_title(md)

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            extract_title("")

    def test_h1_with_extra_hashes(self):
        md = "### Not an h1\n# Valid Title"
        self.assertEqual(extract_title(md), "Valid Title")

if __name__ == "__main__":
    unittest.main()
