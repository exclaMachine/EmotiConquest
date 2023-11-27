import json
import os
import shutil

# Paths to the folders and JSON files
source_folder = 'emoji-images'  # Adjust to your emoji images folder path
destination_folder = 'unshared_emojis'  # Adjust to your desired folder path
unmapped_filenames_json = 'unmapped_filenames.json'  # Path to the unmapped filenames JSON

# Ensure destination folder exists
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Load unmapped filenames
with open(unmapped_filenames_json, 'r') as file:
    unmapped_filenames = set(json.load(file))

# Move files listed in the unmapped filenames JSON to the destination folder
for filename in unmapped_filenames:
    if filename.endswith('.png'):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)
        if os.path.exists(source_path):
            shutil.move(source_path, destination_path)

print("Unmatched emoji images have been moved.")
