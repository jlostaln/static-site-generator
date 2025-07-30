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


if __name__ == "__main__":
    unittest.main()
