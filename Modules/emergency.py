# This module is supposed to be ULTRA-RELIABLE for the user. Like, this module should be able to help
# in case of life-threatening situations.
# You guessed it, it is not yet reliable at all

# import socket
import subprocess
import Modules.audio_ui as audio_ui
import os

RED_CROSS8_IP = "81.92.80.56"
def emergency_resources_reachable(): # checks if the website of the red cross (fr) is reachable
    hostname = RED_CROSS8_IP # example
    response = os.system("ping " + hostname)

    # and then check the response...
    if response == 0:
        return True
    else:
        return False

def process(data): #WIP
    if emergency_resources_reachable():
        print('hi')
        audio_ui.speak("Ressources d'urgence disponibles")
    print('')