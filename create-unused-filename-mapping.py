import json
import os

# Path to the emoji filename mapping JSON and the emoji images folder
filename_mapping_json = 'emoji_filename_mapping.json'
emoji_images_folder = 'emoji-images'  # Update this to your emoji images folder path

# Load the emoji filename mapping
with open(filename_mapping_json, 'r') as file:
    filename_mapping = json.load(file)

# Get the list of actual .png filenames in the emoji images folder
actual_filenames = set(os.listdir(emoji_images_folder))

# Create a set of filenames from the mapping
mapped_filenames = set(filename_mapping.values())

# Find filenames that are in the actual folder but not in the mapping
unmapped_filenames = actual_filenames - mapped_filenames

# Save these unmapped filenames to a new JSON file
with open('unmapped_filenames.json', 'w') as file:
    json.dump(list(unmapped_filenames), file, indent=4)

print(f"Unmapped filenames JSON has been created with {len(unmapped_filenames)} entries.")
