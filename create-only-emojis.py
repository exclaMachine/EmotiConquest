import json

def parse_only_emojis(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    emojis = {}

    for category_data in data.values():
        for subgroup_data in category_data['subgroups'].values():
            for category in subgroup_data['categories'].values():
                for emoji in category['emojis']:
                    emoji_code = emoji[0]  # Unicode codepoint
                    emoji_char = emoji[1]  # The actual emoji character
                    emojis[emoji_code] = emoji_char

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(emojis, file, indent=4)

# Example usage
parse_only_emojis('parsed_emoji_data.json', 'emojis_only.json')
