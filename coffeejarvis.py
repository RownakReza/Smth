import os
import time
import pyttsx3
import speech_recognition as sr



def speak(text):
    engine= pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said
print("Speak")
text = get_audio() 

HELLO_STRS = ["hello jarvis","jarvis", "wake up jarvis"]
for phrase in HELLO_STRS:
    if phrase in text.lower:
        speak("Greetings Sir, how may i assist you")
