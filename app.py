from flask import Flask, request, jsonify
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

app = Flask(__name__)

@app.route('/process_lyrics', methods=['POST'])
def process_lyrics():
    data = request.json
    lyrics = data['lyrics']
    words = word_tokenize(lyrics)
    tagged = nltk.pos_tag(words)
    modified_lyrics = ' '.join(['[' + tag + ']' if word.isalpha() else word for word, tag in tagged])
    return jsonify({"modified_lyrics": modified_lyrics})

if __name__ == '__main__':
    app.run(debug=True)
