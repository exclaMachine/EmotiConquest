import json
import random
import string

def generate_fonts_json():
    fonts = [
        "Arial", "Verdana", "Times New Roman", "Georgia", "Courier New", "Comic Sans MS",
        "Helvetica", "Garamond", "Trebuchet MS", "Impact", "Palatino", "Baskerville",
        "Avant Garde", "Gill Sans", "Tahoma", "Lucida Sans", "Optima", "Perpetua",
        "Futura", "Franklin Gothic", "Roboto", "Lato", "Open Sans", "Montserrat",
        "Source Sans Pro", "Raleway", "Ubuntu", "Merriweather", "Noto Sans", "Playfair Display",
        "Lora", "Arvo", "Josefin Sans", "Alegreya", "Libre Baskerville", "Poppins",
        "Nunito", "Cinzel", "Fjalla One", "PT Sans", "PT Serif", "Old Standard TT",
        "Abril Fatface", "Inconsolata", "Droid Serif", "Droid Sans", "Lobster", "Papyrus",
        # ... other fonts as needed
    ]
    characters = list(string.ascii_uppercase) + list(string.ascii_lowercase) + list(string.digits) + list(string.punctuation)

    # Rarity distribution: 70% common, 25% rare, 5% ultra-rare
    num_fonts = len(fonts)
    common_count = int(0.70 * num_fonts)
    rare_count = int(0.25 * num_fonts)
    ultra_rare_count = num_fonts - common_count - rare_count  # Adjust to ensure total matches

    rarities = (
        ["common"] * common_count +
        ["rare"] * rare_count +
        ["ultra-rare"] * ultra_rare_count
    )
    random.shuffle(rarities)  # Shuffle to distribute rarities randomly

    # Assigning rarities to fonts
    font_rarities = dict(zip(fonts, rarities))

    # Ensuring Papyrus is ultra-rare
    font_rarities["Papyrus"] = "ultra-rare"

    fonts_collection = {
        font: {
            "rarity": font_rarities[font],
            "characters": {char: False for char in characters}
        } for font in fonts
    }

    with open('fonts_collection.json', 'w', encoding='utf-8') as file:
        json.dump(fonts_collection, file, indent=4)

generate_fonts_json()
