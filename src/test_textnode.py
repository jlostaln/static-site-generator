import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_ne_type(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_ne_text(self):
        node = TextNode("Hello world!", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_ne_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_ne_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://wwww.amazon.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_eq_repr(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertEqual("TextNode(This is a text node, bold, https://www.boot.dev)", repr(node)
        )


if __name__ == "__main__":
    unittest.main()
