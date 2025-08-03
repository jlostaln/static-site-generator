
def markdown_to_blocks(markdown):
    block_list = markdown.split("\n\n")
    cleaned_list = []
    for block in block_list:
        if block == "":
            continue
        cleaned_list.append(block.strip())
    return cleaned_list
