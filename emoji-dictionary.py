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
    emoji_dict = {}
    current_group = None
    current_subgroup = None
    current_category = None

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith('# group:'):
                current_group = line.split(': ')[1].strip()
                emoji_dict[current_group] = {
                    "interjection": interjections.get(current_group, "!"),
                    "subgroups": {}
                }
            elif line.startswith('# subgroup:'):
                current_subgroup = line.split(': ')[1].strip()
                if '-' in current_subgroup:
                    current_subgroup, current_category = current_subgroup.split('-', 1)
                else:
                    current_category = 'general'
                emoji_dict[current_group]["subgroups"].setdefault(current_subgroup, {
                    "interjection": interjections.get(current_subgroup, "!"),
                    "categories": {}
                })
                emoji_dict[current_group]["subgroups"][current_subgroup]["categories"].setdefault(current_category, {
                    "interjection": interjections.get(current_category, "!"),
                    "emojis": []
                })
            elif not line.startswith('#') and line.strip():
                parts = line.split(';')
                emoji_code = parts[0].strip().split()[0]
                emoji_and_description = parts[-1].strip().split('# ')[1]
                description = re.sub(r' E\d+\.\d+', '', emoji_and_description)
                emoji_char, _, description_text = description.partition(' ')
                emoticons = emoticons_dict.get(emoji_char, [])
                emoji_dict[current_group]["subgroups"][current_subgroup]["categories"][current_category]["emojis"].append([emoji_code, emoji_char, description_text, emoticons])

    return emoji_dict

# Usage
if __name__ == "__main__":
    emoji_data = parse_emoji_data('emoji-test.txt')

    # Writing to a text file
    with open('parsed_emoji_data.txt', 'w', encoding='utf-8') as file:
        for group, group_data in emoji_data.items():
            file.write(f"Group: {group} - {group_data['interjection']}\n")
            for subgroup, subgroup_data in group_data["subgroups"].items():
                file.write(f"  Subgroup: {subgroup} - {subgroup_data['interjection']}\n")
                for category, category_data in subgroup_data["categories"].items():
                    file.write(f"    Category: {category} - {category_data['interjection']}\n")
                    for emoji_info in category_data["emojis"]:
                        file.write(f"      {emoji_info[1]} ({emoji_info[0]}): {emoji_info[2]}, Emoticons: {', '.join(emoji_info[3])}\n")

    # Writing to JSON file
    with open('parsed_emoji_data.json', 'w', encoding='utf-8') as file:
        json.dump(emoji_data, file, ensure_ascii=False, indent=4)
