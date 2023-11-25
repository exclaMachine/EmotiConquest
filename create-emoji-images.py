import json
from PIL import Image, ImageDraw, ImageFont

def create_emoji_images(json_file, output_folder, font_file, image_size):
    with open(json_file, 'r', encoding='utf-8') as file:
        emojis = json.load(file)

    font = ImageFont.truetype(font_file, image_size)

    for emoji_code, emoji_unicode in emojis.items():
        # Directly decode the Unicode escape sequence
        emoji_char = emoji_unicode.encode('utf-8').decode('unicode-escape')

        # Create an image for each emoji
        image = Image.new('RGBA', (image_size, image_size), (255, 255, 255, 0))
        draw = ImageDraw.Draw(image)
        text_width, text_height = draw.textsize(emoji_char, font=font)
        text_x = (image_size - text_width) // 2
        text_y = (image_size - text_height) // 2
        draw.text((text_x, text_y), emoji_char, font=font, fill=(0, 0, 0, 255))

        # Save the image
        output_path = f"{output_folder}/{emoji_code}.png"
        image.save(output_path)

# Example usage
create_emoji_images('emojis_only.json', 'emoji_images', 'NotoColorEmoji-Regular.ttf', 16)
