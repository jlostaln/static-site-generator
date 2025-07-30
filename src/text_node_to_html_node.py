from textnode import TextNode, TextType

def text_node_to_html_node(textnode: TextNode):
    if not isinstance(textnode.text_type, TextType):
        raise Exception("Invalid textnode.text_type: text_type not a member of TextType enum!")
