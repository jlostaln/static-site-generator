import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_leaf_to_html_witout_tag(self):
        node = LeafNode("", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "Click me!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode("a", "Click me!", {"href": "https://www.google.com"}),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            '<p><b>Bold text</b>Normal text<i>italic text</i><a href="https://www.google.com">Click me!</a>Normal text</p>',
        )

    def test_to_html_empty_children(self):
        node = ParentNode(
            "p",
            [],
        )
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_no_children(self):
        node = ParentNode(
            "p",
            None,
        )
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(
            str(context.exception),
            "Invalid HTML: no children on ParentNode!"
        )

    def test_to_html_without_tag(self):
        node = ParentNode(
            "",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode("a", "Click me!", {"href": "https://www.google.com"}),
                LeafNode(None, "Normal text"),
            ],
        )
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(
            str(context.exception),
            "Invalid HTML: no tag!"
        )

    def test_to_html_leaf_without_value(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", ""),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode("a", "Click me!", {"href": "https://www.google.com"}),
                LeafNode(None, "Normal text"),
            ],
        )
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(
            str(context.exception),
            "Invalid HTML: all leaf nodes must have a value"
        )

if __name__ == "__main__":
    unittest.main()
