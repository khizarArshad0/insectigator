import os
import random
import shutil

# Get the current directory where the script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the directory containing class folders (assuming it's one level up)
dataset_dir = os.path.join(current_dir)

# Desired number of images per class
desired_images_per_class = 70

# Function to randomly delete extra images from a class folder
def balance_class_images(class_dir):
    images = os.listdir(class_dir)
    extra_images = len(images) - desired_images_per_class
    if extra_images > 0:
        random.shuffle(images)
        for i in range(extra_images):
            os.remove(os.path.join(class_dir, images[i]))

# Iterate over each class folder
for class_name in os.listdir(dataset_dir):
    class_dir = os.path.join(dataset_dir, class_name)
    if os.path.isdir(class_dir):
        balance_class_images(class_dir)
