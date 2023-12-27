import json
import random
import string

def generate_fonts_json():
    fonts = [
    "Roboto",
    "Open Sans",
    "Lato",
    "Montserrat",
    "Oswald",
    "Raleway",
    "Noto Sans",
    "Poppins",
    "Ubuntu",
    "Playfair Display",
    "Merriweather",
    "Mukta",
    "Work Sans",
    "Nunito",
    "Fira Sans",
    "Quicksand",
    "Alegreya",
    "Karla"
]


    characters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")

    num_fonts = len(fonts)
    common_count = int(0.70 * num_fonts)
    rare_count = int(0.25 * num_fonts)
    ultra_rare_count = num_fonts - common_count - rare_count

    rarities = (
        ["common"] * common_count +
        ["rare"] * rare_count +
        ["ultra-rare"] * ultra_rare_count
    )
    random.shuffle(rarities)

    font_rarities = dict(zip(fonts, rarities))
    #font_rarities["Papyrus"] = "ultra-rare"

    fonts_list = []
    for font in fonts:
        characters_list = [{"character": char, "collected": False} for char in characters]
        font_data = {
            "name": font,
            "rarity": font_rarities[font],
            "characters": characters_list
        }
        fonts_list.append(font_data)

    fonts_collection = {"fonts": fonts_list}

    with open('fonts_collection.json', 'w', encoding='utf-8') as file:
        json.dump(fonts_collection, file, indent=4)

generate_fonts_json()

def add_new_fonts(file_path, new_fonts):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            fonts_collection = json.load(file)
    except FileNotFoundError:
        fonts_collection = {"fonts": []}

    characters = list(string.ascii_uppercase) + list(string.ascii_lowercase) + list(string.digits) + list(string.punctuation)

    for font in new_fonts:
        if not any(f["name"] == font for f in fonts_collection["fonts"]):
            common_count, rare_count, ultra_rare_count = calculate_rarity_distribution(1)
            rarity = random.choice(["common"] * common_count + ["rare"] * rare_count + ["ultra-rare"] * ultra_rare_count)
            characters_list = [{"character": char, "collected": False} for char in characters]
            font_data = {
                "name": font,
                "rarity": rarity,
                "characters": characters_list
            }
            fonts_collection["fonts"].append(font_data)

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(fonts_collection, file, indent=4)

def calculate_rarity_distribution(num_fonts):
    common_count = int(0.70 * num_fonts)
    rare_count = int(0.25 * num_fonts)
    ultra_rare_count = num_fonts - common_count - rare_count
    return common_count, rare_count, ultra_rare_count

# Example usage
existing_font = "Verdana"
new_public_font = "Open Dyslexic"
#add_new_fonts('fonts_collection.json', [existing_font, new_public_font])
