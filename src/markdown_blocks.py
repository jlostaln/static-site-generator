from enum import Enum
import re

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
