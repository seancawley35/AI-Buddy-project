# import required libraries
from flask import Flask, request, jsonify
from flask_cors import CORS
import buddyRoblox

# create Flask app and enable CORS
app = Flask(__name__)
CORS(app)


@app.route('/Users/seancawley/buddyRoblox.py', methods=['POST'])
def receive_message():
    # Handle incoming messages from client
    message = request.json['message']
    
    # Call chatbot function to generate response
    response = buddyRoblox.generate_response(message)
    
    # Return response as JSON
    return jsonify({'response': response})

@app.route('/response', methods=['POST'])
def send_response():
    # Send response back to client
    pass

# set up route to receive messages from Lua and return response
@app.route('/Users/seancawley/Documents/buddy_avatar.rbxl', methods=['POST'])
def chat():
    # get message from Lua
    data = request.get_json()
    message = data['message']

    # generate response
    response = buddyRoblox.generate_response(message)

    # return response to Lua
    return {'response': response}

if __name__ == '__main__':
    app.run()
