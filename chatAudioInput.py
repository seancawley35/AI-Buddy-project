# import sys
# print(sys.executable)

#text to audio conversion library
import gtts
from playsound import playsound

# Python library to translate
# speech to text and text to speech
import speech_recognition as sr
import pyttsx3

# import openai library
import openai

#string to hold speech
speechString = ""

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to
# speech
def SpeakText(command):
	
	# Initialize the engine
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()



# Set up the OpenAI API client
openai.api_key = ""
greeting = "Hi my name is Buddy!"

ttg = gtts.gTTS(greeting)

# save the audio file
ttg.save("greeting.mp3")

print("Hi my name is Buddy!")
playsound("greeting.mp3")

# this loop will let us ask questions continuously and behave like ChatGPT
while True:
    # Set up the model and prompt
    model_engine = "text-davinci-003"

    # Exception handling to handle
	# exceptions at the runtime
    try:
            # use the microphone as source for input.
            with sr.Microphone() as source2:
                
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.2)
                
                #listens for the user's input
                audio2 = r.listen(source2)
                
                # Using google to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()

                #print("Did you say ",MyText)
                speechString = MyText
                
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
            
    except sr.UnknownValueError:
        print("unknown error occurred")
        
    prompt = speechString

    if 'exit' in prompt or 'quit' in prompt:
        break

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # extracting useful part of response
    response = completion.choices[0].text
    # make request to google to get synthesis
    tts = gtts.gTTS(response)

    # save the audio file
    tts.save("response.mp3")

    

    # printing response
    print(response)
    # play the audio file
    playsound("response.mp3")
