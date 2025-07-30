from htmlnode import LeafNode
from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type: TextType, url=None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other) -> bool:
        return (
                self.text == other.text 
                and self.text_type == other.text_type 
                and self.url == other.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(textnode: TextNode):
    if not isinstance(textnode.text_type, TextType):
        raise ValueError(f"Invalid textnode.text_type: text_type '{textnode.text_type}' not a member of TextType enum!")

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

    return LeafNode(tag, text, props)

