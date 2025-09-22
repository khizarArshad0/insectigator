import os
from PIL import Image
from rembg import remove

def remove_background_from_folder(input_folder, output_folder):
    for class_name in os.listdir(input_folder):
        class_path = os.path.join(input_folder, class_name)
        
        if os.path.isdir(class_path):
            output_class_path = os.path.join(output_folder, class_name)
            if not os.path.exists(output_class_path):
                os.makedirs(output_class_path)

            for image_name in os.listdir(class_path):
                input_image_path = os.path.join(class_path, image_name)
                output_image_path = os.path.join(output_class_path, image_name)

                try:
                    input_image = Image.open(input_image_path)
                    output_image = remove(input_image)

                    if output_image.mode == 'RGBA':
                        output_image = output_image.convert('RGB')
                    
                    output_image.save(output_image_path)
                    print(f"Processed {image_name} successfully.")
                except Exception as e:
                    print(f"Failed to process {image_name}: {str(e)}")


input_folder_train="D:\\Semester 6\\AI\\Project\\Datasets\\ResizedData_70\\ResizedDataset"
output_folder_train="D:\\Semester 6\\AI\\Project\\Datasets\\ResizedData_70\\ResizedTrainingBgRemoved"
input_folder_test = "D:\\Semester 6\\AI\\Project\\Datasets\\ResizedData_70\\ResizedTesting"
output_folder_test = "D:\\Semester 6\\AI\\Project\\Datasets\\ResizedData_70\\ResizedTestingBgRemoved"

remove_background_from_folder(input_folder_train, output_folder_train)
remove_background_from_folder(input_folder_test, output_folder_test)
