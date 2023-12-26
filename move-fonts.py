import os
import shutil

def find_and_move_regular_fonts(source_dir, target_dir):
    # Create target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.lower().endswith('.ttf') and 'regular' in file.lower():
                source_file_path = os.path.join(root, file)
                target_file_path = os.path.join(target_dir, file)
                shutil.move(source_file_path, target_file_path)
                print(f"Moved: {file}")

# Update these paths as per your system
source_directory = '/Users/tyrickers/Downloads/Alegreya,Fira_Sans,Karla,Merriweather,Mukta,etc'  # Path to your font folder
downloads_directory = '/Users/tyrickers/Downloads'  # Path to your Downloads directory
target_directory = os.path.join(downloads_directory, 'Regular-Fonts')

find_and_move_regular_fonts(source_directory, target_directory)
