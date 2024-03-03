# pip install spacy
# python -m spacy download en_core_web_sm



import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

class IntentRecognition:
    def __init__(self):
        # Define simple keyword associations for emotional states
        self.emotion_keywords = {
            'happy': ['happy', 'glad', 'joyful', 'excited'],
            'sad': ['sad', 'depressed', 'unhappy', 'sorrowful'],
            'angry': ['angry', 'mad', 'furious', 'irate'],
        }

    def recognize_emotion(self, text):
        # Process the text with spaCy
        doc = nlp(text.lower())
        # Search for keywords associated with each emotion
        for emotion, keywords in self.emotion_keywords.items():
            if any(keyword in doc.text for keyword in keywords):
                return emotion
        return "neutral"  # Return neutral if no specific emotion is detected

# Example usage
if __name__ == "__main__":
    intent_recognizer = IntentRecognition()
    user_input = "I am so happy to see you!"  # Example text
    detected_emotion = intent_recognizer.recognize_emotion(user_input)
    print(f"Detected emotional intent: {detected_emotion}")
