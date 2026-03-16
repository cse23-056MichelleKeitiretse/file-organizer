import os
import shutil
import sys

def organize_directory(path):
    # Define folder names and their corresponding extensions
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx', '.md'],
        'Audio': ['.mp3', '.wav', '.aac', '.flac'],
        'Video': ['.mp4', '.avi', '.mkv', '.mov'],
        'Archives': ['.zip', '.tar', '.gz', '.rar', '.7z'],
        'Code': ['.py', '.js', '.html', '.css', '.cpp', '.java', '.sh'],
        'Others': []  # everything else
    }

    if not os.path.exists(path):
        print(f"Error: Path '{path}' does not exist.")
        return

    # Move into the directory
    os.chdir(path)

    # Get all files in current directory (ignore folders)
    files = [f for f in os.listdir('.') if os.path.isfile(f)]

    for file in files:
        file_name, file_ext = os.path.splitext(file)
        file_ext = file_ext.lower()

        # Find the right folder
        moved = False
        for folder, extensions in file_types.items():
            if file_ext in extensions:
                dest_folder = folder
                moved = True
                break

        if not moved:
            dest_folder = 'Others'

        # Create folder if it doesn't exist
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)

        # Move file (handle name collisions if needed)
        try:
            shutil.move(file, os.path.join(dest_folder, file))
            print(f"Moved: {file} -> {dest_folder}/")
        except Exception as e:
            print(f"Error moving {file}: {e}")

if __name__ == "__main__":
    # Use command-line argument or default to current directory
    target_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
    organize_directory(target_dir)