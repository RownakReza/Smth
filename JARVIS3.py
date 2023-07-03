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
print("type now")
a = (input())
speak(a)




#I'm beginnin' to feel like a Rap God, Rap God All my people from the front to the back nod, back nodNow, who thinks their arms are long enough to slap box, slap box? They said I rap like a robot, so call me Rap-bot