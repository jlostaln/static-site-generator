import sys
from textnode import TextNode, TextType
from copy_static import copy_static_to_public
from generate_page import generate_page_recursively

dir_path_static = "./static"
dir_path_public = "./docs"
from_path = "./content"
template_path = "./template.html"
dest_path = "./docs"

def main():

    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    copy_static_to_public(dir_path_static, dir_path_public)
    generate_page_recursively(from_path, template_path, dest_path, basepath)


if __name__ == "__main__":
    main()
