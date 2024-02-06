import os
import shutil

def organize_media(source_folder, destination_folder):
    video_folder = os.path.join(destination_folder, 'video')
    image_folder = os.path.join(destination_folder, 'image')
    audio_folder = os.path.join(destination_folder, 'audio')

    os.makedirs(video_folder, exist_ok=True)
    os.makedirs(image_folder, exist_ok=True)
    os.makedirs(audio_folder, exist_ok=True)

    video_counter = 1
    image_counter = 1
    audio_counter = 1

    for root, dirs, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)
            if file.lower().endswith(('.mp4', '.MP4', '.mov', '.MOV', '.avi', '.AVI')):
                new_name = f'{video_counter:03d}.mp4'
                video_counter += 1
                destination_path = os.path.join(video_folder, new_name)
            elif file.lower().endswith(('.jpg', '.jpeg', '.JPG', '.JPEG', '.png', '.PNG')):
                new_name = f'{image_counter:03d}.jpg'
                image_counter += 1
                destination_path = os.path.join(image_folder, new_name)
            elif file.lower().endswith(('.mp3', '.wav', '.flac', '.m4a', '.MP3', '.WAV', '.FLAC', '.M4A')):
                new_name = f'{audio_counter:03d}.m4a'
                audio_counter += 1
                destination_path = os.path.join(audio_folder, new_name)
            else:
                continue

            shutil.move(file_path, destination_path)
            print(f'Moved {file} to {destination_path}')

# Replace 'usb' with the path of your source directory
# Replace 'out' with the path of the folder where you want to organize the media
organize_media('usb', 'out')