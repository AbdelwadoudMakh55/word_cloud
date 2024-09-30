from flask import Flask, jsonify, request, send_from_directory
from word_cloud import generate_text, generate_word_cloud
from flask_cors import CORS

app = Flask(__name__, static_folder='static')
CORS(app)

@app.route('/word_cloud', methods=['POST'])
def word_cloud():
    language = request.json['language']
    text = request.json['text']
    comment_words = generate_text(text)
    return jsonify({"cloud": generate_word_cloud(comment_words, language)})
    
@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(port=5000)