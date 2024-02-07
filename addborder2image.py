import os
from PIL import Image

def analyze_images(image_folder):
    max_width = 0
    max_height = 0

    # Loop through all images in the folder
    for filename in os.listdir(image_folder):
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):  # Add more extensions if needed
            image_path = os.path.join(image_folder, filename)
            image = Image.open(image_path)
            width, height = image.size
            max_width = max(max_width, width)
            max_height = max(max_height, height)

    return max_width, max_height

def add_black_border(image_path, max_width, max_height):
    image = Image.open(image_path)
    width, height = image.size
    new_width = max_width
    new_height = max_height
    horizontal_border = (new_width - width) // 2
    vertical_border = (new_height - height) // 2
    new_image = Image.new(image.mode, (new_width, new_height), color='black')
    new_image.paste(image, (horizontal_border, vertical_border))
    new_image.save("bordered_" + os.path.basename(image_path))

def add_borders_to_all_images(image_folder):
    max_width, max_height = analyze_images(image_folder)
    for filename in os.listdir(image_folder):
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):  # Add more extensions if needed
            image_path = os.path.join(image_folder, filename)
            add_black_border(image_path, max_width, max_height)

# Example usage
image_folder = "images"  # Replace with the path to your image folder
add_borders_to_all_images(image_folder)
