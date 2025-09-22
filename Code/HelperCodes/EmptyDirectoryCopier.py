import os
import shutil

def create_empty_folder_structure(source_folder, destination_folder):
    """
    Create a new folder structure similar to the source folder,
    but without copying any files.
    """
    for root, dirs, files in os.walk(source_folder):
        # Create corresponding directories in the destination folder
        for directory in dirs:
            src_dir = os.path.join(root, directory)
            dst_dir = src_dir.replace(source_folder, destination_folder, 1)
            os.makedirs(dst_dir, exist_ok=True)

# Define source and destination folders
source_folder = "D:\\Semester 6\\AI\\Project\\Datasets\\ResizedDataBgRemoved70\\ResizedTrainingBgRemoved"
destination_folder = "D:\\Semester 6\\AI\\Project\\Datasets\\ResizedDataBgRemoved70\\ResizedRefined"

create_empty_folder_structure(source_folder, destination_folder)
print("Empty folder structure created successfully!")
