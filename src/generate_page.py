import os
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith("# "):
            return line.lstrip("# ").strip()
    raise ValueError("Invalid markdown: No h1 header found!")


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        content = f.read()
    with open(template_path, "r") as f:
        template = f.read()
    html_nodes = markdown_to_html_node(content)
    html_string = html_nodes.to_html()
    title = extract_title(content)
    html_output = template.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
    html_output = html_output.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')

    parent_dir = os.path.dirname(dest_path)
    os.makedirs(parent_dir, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(html_output)

def generate_page_recursively(from_path, template_path, dest_path, basepath):
    for item in os.listdir(from_path):
        source_path = os.path.join(from_path, item) 
        destination_path = os.path.join(dest_path, item).replace(".md", ".html") 

        if os.path.isdir(source_path):
            generate_page_recursively(source_path, template_path, destination_path, basepath)
        else:
            generate_page(source_path, template_path, destination_path, basepath)

