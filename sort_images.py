import os
from PIL import Image
import shutil

def separate_images_by_size(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(input_folder, filename)
            
            try:
                with Image.open(image_path) as img:
                    size_folder = f"{img.width}x{img.height}"
                    size_folder_path = os.path.join(output_folder, size_folder)

                    if not os.path.exists(size_folder_path):
                        os.makedirs(size_folder_path)

                    destination_path = os.path.join(size_folder_path, filename)
                    shutil.move(image_path, destination_path)
                    print("moved")

            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    input_folder_path = "image"
    output_folder_path = "new"

    separate_images_by_size(input_folder_path, output_folder_path)