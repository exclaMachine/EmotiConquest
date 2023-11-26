import json
import re

def parse_only_emojis(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    emoji_dict = {}
    for category_data in data.values():
        for subgroup_data in category_data['subgroups'].values():
            for category in subgroup_data['categories'].values():
                for emoji_info in category['emojis']:
                    emoji_code = emoji_info[0]
                    emoji_char = emoji_info[1]
                    emoji_dict[emoji_code] = emoji_char

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(emoji_dict, file, ensure_ascii=False, indent=4)

# Usage example
parse_only_emojis('parsed_emoji_data.json', 'emojis_only.json')
