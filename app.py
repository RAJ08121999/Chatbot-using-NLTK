import json
import os
from flask import Flask, render_template, request
from nltk.chat.util import Chat, reflections

# Define the path to the dataset
base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, 'data', 'intents.json')

# Load intents from JSON file
with open(data_path, 'r') as file:
    intents = json.load(file)

# Extract patterns and responses from JSON
patterns_responses = []
for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        if pattern.strip():  # Ensure pattern is not empty
            patterns_responses.append((pattern, intent["responses"]))

# Debugging output to check patterns
print("Loaded patterns and responses:")
for pattern, responses in patterns_responses:
    print(f"Pattern: {pattern} - Responses: {responses}")

class SimpleChatbot:
    def __init__(self):
        self.chatbot = Chat(patterns_responses, reflections)

    def get_response(self, user_input):
        return self.chatbot.respond(user_input)

# Initialize the Flask app
app = Flask(__name__)
bot = SimpleChatbot()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET", "POST"])
def get_bot_response():
    user_input = request.args.get('msg')
    return str(bot.get_response(user_input))

if __name__ == "__main__":
    app.run(debug=True)
import json
import os
from flask import Flask, render_template, request
from nltk.chat.util import Chat, reflections
import re

# Define the path to the dataset
base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, 'data', 'intents.json')

# Load intents from JSON file
with open(data_path, 'r') as file:
    intents = json.load(file)

# Extract patterns and responses from JSON
patterns_responses = []
for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        if pattern.strip():  # Ensure pattern is not empty
            patterns_responses.append((pattern, intent["responses"]))

# Debugging output to check patterns
print("Loaded patterns and responses:")
for pattern, responses in patterns_responses:
    print(f"Pattern: {pattern} - Responses: {responses}")

class SimpleChatbot:
    def __init__(self):
        # Add detailed debugging to identify the problematic pattern
        self.chatbot = self._initialize_chatbot(patterns_responses)

    def _initialize_chatbot(self, patterns_responses):
        for pattern, responses in patterns_responses:
            try:
                print(f"Compiling pattern: {pattern}")
                re.compile(pattern, re.IGNORECASE)
            except re.error as e:
                print(f"Error compiling pattern: {pattern}")
                print(f"Error: {e}")
                raise e
        return Chat(patterns_responses, reflections)

    def get_response(self, user_input):
        return self.chatbot.respond(user_input)

# Initialize the Flask app
app = Flask(__name__)
bot = SimpleChatbot()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET", "POST"])
def get_bot_response():
    user_input = request.args.get('msg')
    return str(bot.get_response(user_input))

if __name__ == "__main__":
    app.run(debug=True)
