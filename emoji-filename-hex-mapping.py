import json

def create_filename_mapping(json_file, output_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        emojis = json.load(file)

    filename_mapping = {}
    for code_point, _ in emojis.items():
        # Convert code point to the Noto Emoji filename format
        filename = f"emoji_u{code_point.lower()}.png"
        filename_mapping[code_point] = filename

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(filename_mapping, file, indent=4)

# Usage example
create_filename_mapping('emojis_only.json', 'emoji_filename_mapping.json')
