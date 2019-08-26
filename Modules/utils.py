#Basic.. (bruh)

from time import ctime
import  Modules.audio_ui as audio_ui
import os


def return_current_time():
    return ctime()


def find_location(data):
    data = data.split(" ")
    location = ','.join(data[2:])
    audio_ui.speak("Voici où " + location + " se trouve")
    os.system("start chrome https://www.google.nl/maps/place/" + location + "/&amp;")