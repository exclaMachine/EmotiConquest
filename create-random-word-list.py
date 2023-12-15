import json
import random

def create_random_word_list_json(txt_file_path, json_file_path):
    # Read words from the txt file
    with open(txt_file_path, 'r') as file:
        words = file.read().splitlines()

    # Shuffle the words to create a random order
    random.shuffle(words)

    # Save the words to a json file
    with open(json_file_path, 'w') as json_file:
        json.dump(words, json_file, indent=4)

# Usage
create_random_word_list_json('words_five.txt', 'Random-Words.json')
