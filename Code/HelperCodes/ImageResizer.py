import os
from PIL import Image

# Function to resize images in a directory
def resize_images(input_dir, output_dir, target_size=(224, 224)):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate over each folder (class) in the input directory
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            # Construct the input and output file paths
            input_file = os.path.join(root, file)
            output_file = os.path.join(output_dir, os.path.relpath(input_file, input_dir))

            # Create the output directory for the current file if it doesn't exist
            os.makedirs(os.path.dirname(output_file), exist_ok=True)

            # Open the image
            with Image.open(input_file) as img:
                # Convert image to RGB mode if it's RGBA
                if img.mode == 'RGBA':
                    img = img.convert('RGB')
                
                # Resize the image
                img_resized = img.resize(target_size, Image.Resampling.LANCZOS)
                
                # Save the resized image
                img_resized.save(output_file)

# Input and output directories
input_dir = "D:\\Semester 6\\AI\\Project\\Datasets\\OrignalData\\test"

output_dir = "ResizedTesting"

# Resize images
resize_images(input_dir, output_dir)
