# pip install SpeechRecognition
# pip install PyAudio  # For microphone access


import speech_recognition as sr

def listen_and_stop():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Buddy is listening, you can speak now...")

        # Continuously listen for commands
        while True:
            try:
                # Adjust for ambient noise and record audio
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source)

                # Recognize speech using Google's Web Speech API
                speech_text = recognizer.recognize_google(audio).lower()
                print(f"You said: {speech_text}")

                # Check for stop commands
                if speech_text in ["stop", "exit", "halt"]:
                    print("Stopping Buddy. Goodbye!")
                    break

            except sr.UnknownValueError:
                print("Buddy could not understand the audio. Please try again.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    listen_and_stop()
