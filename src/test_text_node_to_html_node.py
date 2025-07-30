import unittest

from text_node_to_html_node import text_node_to_html_node
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestTextNodeToHTMLNode(unittest.TestCase):

    def test_text_type_not_in_enum(self):
        node = TextNode("This is a text node", "boldanditalic")

        with self.assertRaises(Exception) as context:
            text_node_to_html_node(node)
        self.assertEqual(
            str(context.exception),
            "Invalid textnode.text_type: text_type not a member of TextType enum!"
        )

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("Hello world!", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Hello world!")

    def test_link(self):
        node = TextNode("Click here!", TextType.LINK, "https://www.google.com" )
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click here!")
        self.assertEqual(html_node.props, {"href": "https://www.google.com"})

    def test_image(self):
        node = TextNode("alt text", TextType.IMAGE, "/link/to/image")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "/link/to/image", "alt": "alt text"})


if __name__ == "__main__":
    unittest.main()
