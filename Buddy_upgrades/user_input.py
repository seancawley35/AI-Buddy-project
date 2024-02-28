# pip install SpeechRecognition
# pip install langdetect
# pip install PyAudio  # For microphone input

import speech_recognition as sr
from langdetect import detect

# Initialize recognizer class (for recognizing speech)
recognizer = sr.Recognizer()

def recognize_speech_from_mic(recognizer, microphone):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # Adjust the recognizer sensitivity to ambient noise and record audio
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Please speak now...")
        audio = recognizer.listen(source)

    # Set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None,
        "language": "en-US"  # Default to English
    }

    try:
        # Recognize speech using Google Web Speech API
        response["transcription"] = recognizer.recognize_google(audio, language="en-US")
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # Speech was unintelligible
        response["success"] = False
        response["error"] = "Unable to recognize speech"

    return response

def detect_language_and_recognize_again_if_necessary(response, recognizer, audio):
    if response["transcription"]:
        # Detect the language of the recognized text
        detected_lang = detect(response["transcription"])
        print(f"Detected language: {detected_lang}")

        # You might want to map detected_lang to Google's language codes here

        # If the detected language is different from the initial assumption (English),
        # recognize again with the detected language.
        if detected_lang != "en":
            try:
                # Assuming 'audio' is still accessible and valid for recognition
                response["transcription"] = recognizer.recognize_google(audio, language=detected_lang)
                response["language"] = detected_lang
            except sr.RequestError:
                response["success"] = False
                response["error"] = "API unavailable for detected language"
            except sr.UnknownValueError:
                response["success"] = False
                response["error"] = "Unable to recognize speech in detected language"
    else:
        print("No transcription available to detect language from.")

    return response

# Main function to orchestrate the speech recognition and language detection
def main():
    print("Starting program...")
    with sr.Microphone() as source:
        initial_response = recognize_speech_from_mic(recognizer, source)
        if initial_response["success"] and not initial_response["error"]:
            print(f"Initial transcription: {initial_response['transcription']}")
            final_response = detect_language_and_recognize_again_if_necessary(initial_response, recognizer, source)
            print(f"Final Transcription: {final_response['transcription']}")
            print(f"Language: {final_response['language']}")
        else:
            print(f"Error: {initial_response['error']}")

main()



