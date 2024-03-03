

# import sys
# print(sys.executable)

#text to audio conversion library
import gtts
from playsound import playsound

# import openai library
import openai

# Set up the OpenAI API client
openai.api_key = ""
greeting = "Hi my name is Buddy!"

ttg = gtts.gTTS(greeting)

# save the audio file
ttg.save("greeting.mp3")

print("Hi my name is Buddy!")
playsound("greeting.mp3")

def generate_response():
    # this loop will let us ask questions continuously and behave like ChatGPT
    while True:
        # Set up the model and prompt
        model_engine = "text-davinci-003"
        
        prompt = input('Enter Prompt:')

        if 'exit' in prompt or 'quit' in prompt:
            break

        # Generate a responseH
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
        
generate_response()
