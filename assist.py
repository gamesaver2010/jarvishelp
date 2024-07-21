import os
from groq import Groq
from pygame import mixer
import time
client = Groq(
    api_key=("api_key"),
)
def hey_jarvis():
    text=input("Hello sir, how can I help you?")   
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are an assistant named Jarvis like from the Iron Man movies. You are to act like him and provide help as best as you can, keep it brief and serious in your responses. At the ending of each response you must say is there anything else you need help with?"
            },
            {
                "role": "user",
                "content":text,
            }, 

        ],
    
     model="llama3-8b-8192",

        )

    print(chat_completion.choices[0].message.content)

def generate_tts(sentence, speech_file_path):
    response = client.audio.speech.create(model="tts-1", voice="echo", input=sentence)
    response.stream_to_file(speech_file_path)
    return str(speech_file_path)

def play_sound(file_path):
    mixer.music.load(file_path)
    mixer.music.play()

def TTS(text):
    speech_file_path = generate_tts(text, "speech.mp3")
    play_sound(speech_file_path)
    while mixer.music.get_busy():
        time.sleep(1)
    mixer.music.unload()
    os.remove(speech_file_path)
    return "done"





