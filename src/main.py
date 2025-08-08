from textnode import TextNode, TextType
from copy_static import copy_static_to_public
from generate_page import generate_page

dir_path_static = "./static"
dir_path_public = "./public"
from_path = "./content/index.md"
template_path = "./template.html"
dest_path = "./public/index.html"

def main():

    copy_static_to_public(dir_path_static, dir_path_public)
    generate_page(from_path, template_path, dest_path)



if __name__ == "__main__":
    main()
