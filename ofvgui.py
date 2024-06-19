import os
import shutil
from pathlib import Path
import tkinter as tk
from tkinter import filedialog

def organize_files():
    # Get the selected directory from the user
    directory = Path(dir_entry.get())

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

# Create the GUI window
window = tk.Tk()
window.title("File Organizer")

# Create a label and entry field for the directory
dir_label = tk.Label(window, text="Enter the directory path:")
dir_label.pack()
dir_entry = tk.Entry(window, width=50)
dir_entry.pack()

# Create a button to browse for the directory
browse_button = tk.Button(window, text="Browse", command=lambda: dir_entry.insert(0, filedialog.askdirectory()))
browse_button.pack()

# Create a button to start organizing files
organize_button = tk.Button(window, text="Organize Files", command=organize_files)
organize_button.pack()

# Run the GUI event loop
window.mainloop()