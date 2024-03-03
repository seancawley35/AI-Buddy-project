# pip install SpeechRecognition
# pip install PyAudio  # For microphone access


import speech_recognition as sr

class BuddyChatbot:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            print("Buddy is listening, please speak...")
            # Adjusting for ambient noise can help reduce errors
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

            try:
                # Using Google Web Speech API for example
                text = self.recognizer.recognize_google(audio)
                print("You said: " + text)
                # Here you would add functionality to process the input and generate a response
                self.respond(text)
            except sr.UnknownValueError:
                print("Buddy could not understand the audio.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

    def respond(self, text):
        # Placeholder for response logic
        print(f"Buddy's response placeholder to: '{text}'")

if __name__ == "__main__":
    buddy = BuddyChatbot()
    buddy.listen()

