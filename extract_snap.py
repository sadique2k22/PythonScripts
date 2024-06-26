import os
import shutil
from datetime import date
from PIL import Image
import subprocess
from tqdm import tqdm

# Step 1: Get today's date
#today = date(2024,6,21)
today = date.today()
today_str = today.strftime("%d-%m-%Y")

# Step 2: Specify directories
source_dir = "/data/data/com.snapchat.android/files/native_content_manager/"
destination_dir = f"/storage/emulated/0/snap/{today_str}"
image_dir = os.path.join(destination_dir, f"/storage/emulated/0/snap/{today_str}/images")
video_dir = os.path.join(destination_dir, f"/storage/emulated/0/snap/{today_str}/videos")

# Step 3: Create destination directories
os.makedirs(destination_dir, exist_ok=True)
os.makedirs(image_dir, exist_ok=True)
os.makedirs(video_dir, exist_ok=True)

# Step 4: Collect all files
all_files = []
for root, dirs, files in os.walk(source_dir):
    for file in files:
        file_path = os.path.join(root, file)
        all_files.append(file_path)

# Step 5-7: Process files with progress bar
for file_path in tqdm(all_files, desc="Processing files", unit="file"):
    # Check if file was created today
    if date.fromtimestamp(os.path.getmtime(file_path)) == today:
        # Step 5: Check if file is an image using PIL
        try:
            with Image.open(file_path) as img:
                # Step 6: Move images to "images" folder and convert to PNG
                img.save(os.path.join(image_dir, f"{os.path.basename(file_path)}.png"))
                continue  # Skip to next file
        except:
            pass
        
        # Step 7: Check if file is a video using ffmpeg
        result = subprocess.run(['ffmpeg', '-i', file_path], stderr=subprocess.PIPE)
        output = result.stderr.decode()
        if 'Video' in output:
            # Move videos to "videos" folder and convert to MP4
            new_file_name = os.path.splitext(os.path.basename(file_path))[0] + ".mp4"
            shutil.move(file_path, os.path.join(video_dir, new_file_name))
        else:
            # If not an image or video, skip the file
            continue
        