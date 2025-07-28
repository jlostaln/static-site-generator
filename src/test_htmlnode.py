import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):

    def test_eq(self):
        node = HTMLNode("a", "link", None, {"href": "https://www.google.com", "target": "_blank",})
        node2 = HTMLNode("a", "link", props={"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(node, node2)

    def test_ne(self):
        node = HTMLNode("a", "link", None, {"href": "https://www.google.com", "target": "_blank",})
        node2 = HTMLNode("p", "this is text in paragraph")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = HTMLNode("a", "link", None, {"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual("HTMLNode(a, link, children: None, {'href': 'https://www.google.com', 'target': '_blank'})", node.__repr__())

    def test_props_to_html(self):
        node = HTMLNode("a", "link", None, {"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(' href="https://www.google.com" target="_blank"', node.props_to_html())

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

if __name__ == "__main__":
    unittest.main()
