import os
import shutil

def move_jpg_files(source_folder, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    files = os.listdir(source_folder)
    for file in files:
        if file.endswith('.jpg'):
            shutil.move(os.path.join(source_folder, file), os.path.join(dest_folder, file))
    print(f"Moved all .jpg files from {source_folder} to {dest_folder}")

# Example usage:
source = "source_folder_path"
destination = "destination_folder_path"
move_jpg_files(source, destination)
