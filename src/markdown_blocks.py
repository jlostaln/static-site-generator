from enum import Enum
import re

from htmlnode import ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from inline_markdown import text_to_textnodes

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block):
    lines = block.splitlines()

    if re.findall(r"^#{1,6} ", lines[0]) != []:
        return BlockType.HEADING

    if lines[0].startswith("```") and lines[-1].endswith("```"):
        return BlockType.CODE

    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE

    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST

    if block.startswith("1. "):
        for i in range(len(lines)):
            if not lines[i].startswith(f"{i+1}. "):
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH


def markdown_to_blocks(markdown):
    block_list = markdown.split("\n\n")
    cleaned_list = []
    for block in block_list:
        if block == "":
            continue
        cleaned_list.append(block.strip())
    return cleaned_list


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def heading_to_html_node(text):
    matches = re.findall(r"^#{1,6} ", text)
    text = re.sub(r"^#{1,6}\s+", "", text) 
    heading = matches[0].strip()
    tag = f"h{len(heading)}"
    children = text_to_children(text)
    return ParentNode(tag, children)


def quote_to_html_node(text):
    text = re.sub(r"^[\>]\s+", "", text, flags=re.MULTILINE).split("\n")
    new_lines = []
    for item in text:
        new_lines.append(item)
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)


def unordered_list_to_html_node(text):
    text = re.sub(r"^[\-]\s+", "", text, flags=re.MULTILINE)
    html_items = []
    for item in text.split("\n"):
        children = text_to_children(item)
        html_items.append(handle_item_in_list(children))
    return ParentNode("ul", html_items)


def ordered_list_to_html_node(text):
    text = re.sub(r"^\d+\.\s+", "", text, flags=re.MULTILINE)
    html_items = []
    for item in text.split("\n"):
        children = text_to_children(item)
        html_items.append(handle_item_in_list(children))
    return ParentNode("ol", html_items)


def handle_item_in_list(children):
    return ParentNode("li", children)


def paragraph_to_html_node(text):
    paragraph = " ".join(text.split("\n"))
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def code_to_html_node(text):
    text = text.strip("```").lstrip()
    text_node = TextNode(text, TextType.TEXT)
    return ParentNode("pre", [ParentNode("code", [text_node_to_html_node(text_node)])])


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.HEADING:
                nodes.append(heading_to_html_node(block)) 
            case BlockType.QUOTE:
                nodes.append(quote_to_html_node(block)) 
            case BlockType.UNORDERED_LIST:
                nodes.append(unordered_list_to_html_node(block)) 
            case BlockType.ORDERED_LIST:
                nodes.append(ordered_list_to_html_node(block)) 
            case BlockType.PARAGRAPH:
                nodes.append(paragraph_to_html_node(block))
            case BlockType.CODE:
                nodes.append(code_to_html_node(block))
    root = ParentNode("div", nodes)
    return root
