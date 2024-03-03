#pip install Flask

from flask import Flask, render_template, request, jsonify
import response_generation  # Assuming this is your module for generating responses

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # HTML file to render the text box

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get('user_input')
    response = response_generation.get_response(user_input)  # Get response from your module
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

