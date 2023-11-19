import json
import re

def parse_emoji_data(file_path):
    emoji_dict = {}
    current_group = None
    current_subgroup = None
    current_category = None

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith('# group:'):
                current_group = line.split(': ')[1].strip()
                emoji_dict[current_group] = {}
            elif line.startswith('# subgroup:'):
                current_subgroup = line.split(': ')[1].strip()
                # Splitting the subgroup to extract the category
                if '-' in current_subgroup:
                    current_subgroup, current_category = current_subgroup.split('-', 1)
                else:
                    current_category = 'general'  # Default category if no hyphen
                if current_subgroup not in emoji_dict[current_group]:
                    emoji_dict[current_group][current_subgroup] = {}
                if current_category not in emoji_dict[current_group][current_subgroup]:
                    emoji_dict[current_group][current_subgroup][current_category] = []
            elif not line.startswith('#') and line.strip():
                parts = line.split(';')
                emoji = parts[0].strip().split()[0]  # Assuming the first part is the emoji
                description = parts[-1].strip().split('# ')[1]  # Assuming description is after '#'
                description = re.sub(r' E\d+\.\d+', '', description)  # Removing the "E" designation
                emoji_dict[current_group][current_subgroup][current_category].append((emoji, description))

    return emoji_dict

# Usage
if __name__ == "__main__":
    emoji_data = parse_emoji_data('emoji-test.txt')

    # Writing to a file
    with open('parsed_emoji_data.txt', 'w', encoding='utf-8') as file:
        for group, subgroups in emoji_data.items():
            file.write(f"Group: {group}\n")
            for subgroup, categories in subgroups.items():
                file.write(f"  Subgroup: {subgroup}\n")
                for category, emojis in categories.items():
                    file.write(f"    Category: {category}\n")
                    for emoji, description in emojis:
                        file.write(f"      {emoji}: {description}\n")

    with open('parsed_emoji_data.json', 'w', encoding='utf-8') as file:
        json.dump(emoji_data, file, ensure_ascii=False, indent=4)
