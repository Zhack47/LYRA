import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
from Modules.identification import username
import Modules.emergency as emergency
import Modules.audio_ui as audio_ui


def file(data):
    if "how are you" in data:
        audio_ui.speak("I am fine")

    if "what time is it" in data:
        audio_ui.speak(ctime())

    if "where is" in data:
        data = data.split(" ")
        location = ','.join(data[2:])
        audio_ui.speak("Hold on " +username + ", I will show you where " + location + " is.")
        print(location)
        os.system("start chrome https://www.google.nl/maps/place/" + location + "/&amp;")
    if "emergency mode" in data:
        emergency.process(data)
# initialization
time.sleep(2)
audio_ui.speak("Hi "+ username + ", what can I do for you?")

while 1:
    data = audio_ui.recordAudio()
    file(data)