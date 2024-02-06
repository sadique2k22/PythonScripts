import os

def rename_files_by_size(folder_path):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    files.sort(key=lambda f: os.path.getsize(os.path.join(folder_path, f)))

    for i, file_name in enumerate(files, start=1):
        old_path = os.path.join(folder_path, file_name)
        new_name = f"{i}.jpg"
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)
        print(f"Renamed: {file_name} to {new_name}")

# Replace 'path_to_your_folder' with the actual path of your folder containing the images
folder_path = '/storage/emulated/0/Android/data/org.thunderdog.challegram/files/photos/'
rename_files_by_size(folder_path)