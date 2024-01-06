import nltk
from nltk.tokenize import word_tokenize

def tag_parts_of_speech(lyrics):
    words = word_tokenize(lyrics)
    tagged = nltk.pos_tag(words)
    return ' '.join(['[' + tag + ']' if word.isalpha() else word for word, tag in tagged])

# Sample lyrics for testing
lyrics = "Twinkle, twinkle, little star, How I wonder what you are"

# Process the lyrics
modified_lyrics = tag_parts_of_speech(lyrics)

# Print the original and modified lyrics
print("Original Lyrics:\n", lyrics)
print("\nModified Lyrics:\n", modified_lyrics)
