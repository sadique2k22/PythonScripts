import os
import shutil
from datetime import date, datetime
from PIL import Image
import subprocess
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

# Step 1: Get today's date
#today = date(2024,7,6) #remove # and write custom date in yyyy-mm-dd format
today = date.today() #add a # in the beginning if you want to use custom date
today_str = today.strftime("%d-%m-%Y")

# Step 2: Specify directories
source_dir = "/data/data/com.snapchat.android/files/native_content_manager/"
destination_dir = f"/storage/emulated/0/snap/{today_str}"
image_dir = os.path.join(destination_dir, "images")
video_dir = os.path.join(destination_dir, "videos")
audio_dir = os.path.join(destination_dir, "audios")

# Step 3: Create destination directories
os.makedirs(image_dir, exist_ok=True)
os.makedirs(video_dir, exist_ok=True)
os.makedirs(audio_dir, exist_ok=True)

# Step 4: Collect all files
all_files = []
for root, dirs, files in os.walk(source_dir):
    for file in files:
        file_path = os.path.join(root, file)
        all_files.append(file_path)

def is_voice_note(file_path):
    try:
        # Use ffmpeg to get the file type
        result = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', 
                                 '-of', 'default=noprint_wrappers=1:nokey=1', file_path], 
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        duration_str = result.stdout.decode().strip()
        duration = float(duration_str)
        
        result = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'a', 
                                 '-show_entries', 'stream=codec_type', 
                                 '-of', 'default=noprint_wrappers=1:nokey=1', file_path], 
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        codec_type = result.stdout.decode().strip()

        if codec_type == 'audio' and duration <= 180:
            return True
    except:
        # Suppress the errors
        return False
    return False

def file_created_today(file_path):
    file_creation_time = datetime.fromtimestamp(os.path.getctime(file_path)).date()
    return file_creation_time == today

def handle_file_overwrite(file_path):
    base, ext = os.path.splitext(file_path)
    counter = 1
    new_file_path = file_path
    while os.path.exists(new_file_path):
        new_file_path = f"{base}_{counter}{ext}"
        counter += 1
    return new_file_path

def process_file(file_path):
    try:
        # Check if file was created today
        if file_created_today(file_path):
            # Step 5: Check if file is an image using PIL
            try:
                with Image.open(file_path) as img:
                    # Skip images with dimensions less than 641 on each side
                    if img.width < 641 or img.height < 641:
                        return
                    # Step 6: Move images to "images" folder and convert to PNG
                    new_image_path = os.path.join(image_dir, f"{os.path.basename(file_path)}.png")
                    new_image_path = handle_file_overwrite(new_image_path)
                    img.save(new_image_path)
                    return
            except:
                pass

            # Step 7: Check if file is a video using ffmpeg
            result = subprocess.run(['ffmpeg', '-i', file_path], stderr=subprocess.PIPE)
            output = result.stderr.decode()
            if 'Video' in output:
                # Copy videos to "videos" folder and convert to MP4
                new_file_name = os.path.splitext(os.path.basename(file_path))[0] + ".mp4"
                new_file_path = os.path.join(video_dir, new_file_name)
                new_file_path = handle_file_overwrite(new_file_path)
                shutil.copy(file_path, new_file_path)
            elif is_voice_note(file_path):
                # Step 8: Copy voice notes to "audios" folder and add .mp3 extension
                new_file_name = os.path.basename(file_path) + ".mp3"
                new_file_path = os.path.join(audio_dir, new_file_name)
                new_file_path = handle_file_overwrite(new_file_path)
                shutil.copy(file_path, new_file_path)
    except:
        # Suppress any errors silently
        pass

# Step 5-8: Process files with progress bar using ThreadPoolExecutor
with ThreadPoolExecutor() as executor:
    futures = [executor.submit(process_file, file_path) for file_path in all_files]
    for future in tqdm(as_completed(futures), total=len(futures), desc="Processing files", unit="file"):
        pass
