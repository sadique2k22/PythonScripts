import os
import shutil

source_directory = "/storage/emulated/0/Android/data/org.thunderdog.challegram/files/photos/"
destination_directory = "/storage/emulated/0/Download/shorts/tg/"

# Make sure the destination directory exists
os.makedirs(destination_directory, exist_ok=True)

# Loop through files in the source directory
for filename in os.listdir(source_directory):
    source_path = os.path.join(source_directory, filename)
    destination_path = os.path.join(destination_directory, filename)

    # Check if the file is an image (you can adjust the extensions as needed)
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        shutil.move(source_path, destination_path)
        print("Image moved successfully.")
        
print("ALL DONE")