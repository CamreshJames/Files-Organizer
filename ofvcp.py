import os
import shutil
from pathlib import Path

# Ask the user for the directory to organize
user_dir = input("Enter the directory path you want to organize (e.g., C:/Users/Username/Desktop): ")
directory = Path(user_dir)

# Define the extensions to categorize
video_extensions = [".mp4", ".avi", ".mkv", ".mov"]
music_extensions = [".mp3", ".wav", ".flac", ".aac"]
compressed_extensions = [".zip", ".rar", ".7z", ".tar.gz"]
app_extensions = [".exe", ".msi", ".app", ".dmg"]
doc_extensions = [".doc", ".docx", ".pdf", ".txt", ".xlsx", ".pptx"]

# Create directories for each category if they don't exist
video_dir = directory / "Videos"
music_dir = directory / "Music"
compressed_dir = directory / "Compressed"
app_dir = directory / "Applications"
doc_dir = directory / "Documents"
shortcuts_dir = directory / "Shortcuts"

for category_dir in [video_dir, music_dir, compressed_dir, app_dir, doc_dir, shortcuts_dir]:
    if not category_dir.exists():
        category_dir.mkdir()

# Loop through all files in the specified directory
for file in directory.iterdir():
    if file.is_file() and file.name not in ["PC", "Recycle Bin"]:
        extension = file.suffix.lower()

        # Move the file to the appropriate directory
        if extension in video_extensions:
            dest_path = video_dir / file.name
            shutil.move(str(file), str(dest_path))
            print(f"Moved {file.name} to {video_dir}")
        elif extension in music_extensions:
            dest_path = music_dir / file.name
            shutil.move(str(file), str(dest_path))
            print(f"Moved {file.name} to {music_dir}")
        elif extension in compressed_extensions:
            dest_path = compressed_dir / file.name
            shutil.move(str(file), str(dest_path))
            print(f"Moved {file.name} to {compressed_dir}")
        elif extension in app_extensions:
            dest_path = app_dir / file.name
            shutil.move(str(file), str(dest_path))
            print(f"Moved {file.name} to {app_dir}")
        elif extension in doc_extensions:
            dest_path = doc_dir / file.name
            shutil.move(str(file), str(dest_path))
            print(f"Moved {file.name} to {doc_dir}")
        else:
            dest_path = shortcuts_dir / file.name
            shutil.move(str(file), str(dest_path))
            print(f"Moved {file.name} to {shortcuts_dir}")