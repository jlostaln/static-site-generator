import os
import shutil

def copy_static_to_public(source, destination):

    if os.path.exists(destination):
        shutil.rmtree(destination)
        print(f"Removed {destination} and its content")
    os.mkdir(destination)
    print(f"Directory {destination} created")

    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)

        if os.path.isdir(source_path):
            # os.mkdir(destination_path)
            # print(f"Directory {destination_path} copied.")
            copy_static_to_public(source_path, destination_path)
        else:
            shutil.copy(source_path, destination_path)
            print(f"File copied: {source_path} -> {destination_path}")
