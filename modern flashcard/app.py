from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

def load_flashcards():
    """Load flashcards from JSON file."""
    try:
        with open('flashcards.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_flashcards(flashcards):
    """Save flashcards to JSON file."""
    with open('flashcards.json', 'w') as file:
        json.dump(flashcards, file)

@app.route('/')
def home():
    """Render the home page with the form to add flashcards."""
    return render_template('index.html')

@app.route('/flashcards')
def flashcards_page():
    """Render the page displaying all flashcards."""
    flashcards = load_flashcards()
    return render_template('flashcards.html', flashcards=flashcards)

@app.route('/add_flashcard', methods=['POST'])
def add_flashcard():
    """Add a new flashcard and redirect to the flashcards page."""
    flashcards = load_flashcards()
    question = request.form['question']
    answer = request.form['answer']
    flashcards.append({'question': question, 'answer': answer})
    save_flashcards(flashcards)
    return jsonify({'status': 'Flashcard added successfully!', 'redirect': '/flashcards'})

@app.route('/get_flashcards', methods=['GET'])
def get_flashcards():
    """Retrieve all flashcards."""
    flashcards = load_flashcards()
    return jsonify(flashcards)

if __name__ == '__main__':
    app.run(debug=True)
