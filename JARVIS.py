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
print("Speak now")
text = get_audio()


if "Hello" in text:
    speak("Greetings sir, how may i assist you")

if "Jarvis" in text:
    speak("Greetings sir, how may i assist you")

if "emergency" in text:
    speak("Initiating emegency protocol, closing all exit, dispating police units to current location")

if "how are you" in text:
    speak("I am fine, How are you")




