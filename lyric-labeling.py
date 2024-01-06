import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def tag_parts_of_speech(lyrics):
    words = word_tokenize(lyrics)
    tagged = nltk.pos_tag(words)
    return ' '.join(['[' + tag + ']' if word.isalpha() else word for word, tag in tagged])

lyrics = "Twinkle, twinkle, little star, How I wonder what you are"
modified_lyrics = tag_parts_of_speech(lyrics)
print(modified_lyrics)
