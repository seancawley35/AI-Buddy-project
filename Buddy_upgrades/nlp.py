pip install spacy
python -m spacy download en_core_web_sm

import spacy
from user_input import get_user_input  # Import the function from user_input.py

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

class BuddyNLP:
    def __init__(self):
        self.responses = {
            'greet': 'Hello! How can I help you today?',
            'thank': 'You\'re welcome!',
            'bye': 'Goodbye! Have a great day!',
        }
        self.default_response = 'I\'m not sure how to respond to that.'

    def understand_intent(self, text):
        # Process the text with spaCy
        doc = nlp(text)

        # Try to identify the intent based on the main verb and subject in the sentence
        for token in doc:
            if token.dep_ == 'ROOT' or (token.dep_ == 'aux' and token.head.dep_ == 'ROOT'):
                # Simplistic way to determine intent
                if token.lemma_ in ['greet', 'hello', 'hi']:
                    return 'greet'
                elif token.lemma_ in ['thank', 'thanks']:
                    return 'thank'
                elif token.lemma_ in ['bye', 'goodbye']:
                    return 'bye'
        
        return None

    def generate_response(self, intent):
        return self.responses.get(intent, self.default_response)

    def respond(self, user_input):
        intent = self.understand_intent(user_input)
        response = self.generate_response(intent)
        return response

# Example usage
if __name__ == "__main__":
    buddy = BuddyNLP()
    user_input = get_user_input()  # Get user input from the user_input.py file
    response = buddy.respond(user_input)
    print("Buddy:", response)
