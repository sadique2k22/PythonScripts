import os
import shutil
import subprocess
subprocess.run(["pkg", "install", "python", "-y"])
subprocess.run(["pkg", "install", "python-pillow", "-y"])
subprocess.run(["pip", "install", "tqdm"])
subprocess.run(["pkg", "install", "ffmpeg", "-y"])
subprocess.run(["pip", "install", "ffmpeg"])
from PIL import Image
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
source_dir = "/data/data/com.whatsapp/"
destination_dir = f"/sdcard/output/whatsapp/"
image_dir = os.path.join(destination_dir, "images")
video_dir = os.path.join(destination_dir, "videos")
os.makedirs(destination_dir, exist_ok=True)
os.makedirs(image_dir, exist_ok=True)
os.makedirs(video_dir, exist_ok=True)
all_files = []
for root, dirs, files in os.walk(source_dir):
    for file in files:
        file_path = os.path.join(root, file)
        all_files.append(file_path)
def process_file(file_path):
    try:
        with Image.open(file_path) as img:
            img.save(os.path.join(image_dir, f"{os.path.basename(file_path)}.png"))
            return 
    except:
        pass
    result = subprocess.run(['ffmpeg', '-i', file_path], stderr=subprocess.PIPE)
    output = result.stderr.decode()
    if 'Video' in output:
        new_file_name = os.path.splitext(os.path.basename(file_path))[0] + ".mp4"
        shutil.copy(file_path, os.path.join(video_dir, new_file_name))
    else:
        return
with ThreadPoolExecutor(max_workers=50) as executor:
    list(tqdm(executor.map(process_file, all_files), total=len(all_files), desc="Processing files", unit="file"))