from htmlnode import LeafNode
from textnode import TextNode, TextType

def text_node_to_html_node(textnode: TextNode):
    if not isinstance(textnode.text_type, TextType):
        raise Exception("Invalid textnode.text_type: text_type not a member of TextType enum!")

    props = None
    text = textnode.text
    match textnode.text_type:
        case TextType.TEXT:
            tag = None
        case TextType.BOLD:
            tag = "b"
        case TextType.ITALIC:
            tag = "i"
        case TextType.CODE:
            tag = "code"
        case TextType.LINK:
            tag = "a"
            props = {"href": textnode.url} 
        case TextType.IMAGE:
            tag = "img"
            props = {"src": textnode.url, "alt": text}
            text = ""

    print(LeafNode(tag, text, props))
    return LeafNode(tag, text, props)
