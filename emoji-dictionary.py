import json
import re

# Dictionary of interjections
interjections = {
    "Food & Drink": "Delicious!",
    "food": "Nom Nom!",
    "fruit": "Sweet!",
    "animal": "Cute!",
    "vegetable": "Healthy!",
    "cat": "Meow!",
    # ... add more mappings as needed
}

# Predefined dictionary for emoticons
emoticons_dict = {
    "😀": [":^)", ":)", "=)", ":-)", "=-)"],
    "😁": [":D", ":-D", "=D"],
    "😠": [">:[", ">:("],
    # Add more emojis and corresponding emoticons here
    # ...
}

def parse_emoji_data(file_path):
    emoji_data = {"groups": []}
    current_group = None
    current_subgroup = None
    current_category = None
    processed_codes = set()  # Set to keep track of processed codes

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith('# group:'):
                current_group = {
                    "name": line.split(': ')[1].strip(),
                    "interjection": interjections.get(line.split(': ')[1].strip(), "!"),
                    "subgroups": []
                }
                emoji_data["groups"].append(current_group)
            elif line.startswith('# subgroup:'):
                current_subgroup = {
                    "name": line.split(': ')[1].strip(),
                    "categories": []
                }
                current_group["subgroups"].append(current_subgroup)
            elif not line.startswith('#') and line.strip():
                parts = line.split(';')
                emoji_code = parts[0].strip().split()[0]
                # Skip if emoji code has already been processed
                if emoji_code in processed_codes:
                    continue
                processed_codes.add(emoji_code)
                emoji_char_and_description = parts[-1].strip().split('# ')[1]
                description = re.sub(r' E\d+\.\d+', '', emoji_char_and_description)
                emoji_char, _, description_text = description.partition(' ')
                emoticons = emoticons_dict.get(emoji_char, [])
                emoji_info = {
                    "code": emoji_code,
                    "character": emoji_char,
                    "description": description_text.strip(),
                    "emoticons": emoticons
                }
                if '-' in current_subgroup["name"]:
                    current_subgroup_name, current_category_name = current_subgroup["name"].split('-', 1)
                else:
                    current_subgroup_name = current_subgroup["name"]
                    current_category_name = 'general'
                # Find or create the category
                category = next((cat for cat in current_subgroup["categories"] if cat["name"] == current_category_name), None)
                if not category:
                    category = {"name": current_category_name, "interjection": interjections.get(current_category_name, "!"), "emojis": []}
                    current_subgroup["categories"].append(category)
                category["emojis"].append(emoji_info)

    return emoji_data

# Usage
if __name__ == "__main__":
    emoji_data = parse_emoji_data('emoji-test.txt')

    # Writing to JSON file
    with open('parsed_emoji_data.json', 'w', encoding='utf-8') as file:
        json.dump(emoji_data, file, ensure_ascii=False, indent=4)
