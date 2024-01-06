import nltk
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Mapping from NLTK's POS tags to full names
tag_full_names = {
    'NN': 'noun',
    'NNS': 'noun(plural)',
    'NNP': 'proper noun',
    'NNPS': 'proper noun(plural)',
    'VB': 'verb(base form)',
    'VBD': 'verb(past tense)',
    'VBG': 'verb(gerund/present participle)',
    'VBN': 'verb(past participle)',
    'VBP': 'verb(singular present)',
    'VBZ': 'verb(3rd person singular present)',
    'JJ': 'adjective',
    'JJR': 'adjective(comparative)',
    'JJS': 'adjective(superlative)',
    'RB': 'adverb',
    'RBR': 'adverb(comparative)',
    'RBS': 'adverb(superlative)',
    # Add more tags as needed
}

def tag_parts_of_speech(lyrics):
    words = word_tokenize(lyrics)
    tagged = nltk.pos_tag(words)
    return ' '.join(['[' + tag_full_names.get(tag, word) + ']' if word.isalpha() else word for word, tag in tagged])

# Sample lyrics for testing
#lyrics = "Twinkle, twinkle, little star, How I wonder what you are"
lyrics = """When we were young, the future was so bright Woah-oh The old neighborhood was so alive Woah-oh And every kid on the whole damn street
Woah-oh
Was gonna make it big and not be beat
Now the neighborhood's cracked and torn
Woah-oh
The kids are grown up, but their lives are worn
Woah-oh
How can one little street swallow so many lives?
Chances thrown
Nothing's free
Longing for, used to be
Still it's hard, hard to see
Fragile lives
Shattered dreams (go!)
Jamie had a chance, well, she really did
Woah-oh
Instead she dropped out and had a couple of kids
Woah-oh
Mark still lives at home 'cause he's got no job
Woah-oh
He just plays guitar and smokes a lot of pot
Jay commited suicide
Woah-oh
Brandon OD'd and died
Woah-oh
What the hell is going on?
The cruelest dream, reality
Chances thrown
Nothing's free
Longing for, used to be
Still it's hard, hard to see
Fragile lives
Shattered dreams (Go!)
Chances thrown
Nothing's free
Longing for (what), used to be
Still it's hard, hard to see
Fragile lives
Shattered dreams
"""
# Process the lyrics
modified_lyrics = tag_parts_of_speech(lyrics)

# Print the original and modified lyrics
print("Original Lyrics:\n", lyrics)
print("\nModified Lyrics:\n", modified_lyrics)
