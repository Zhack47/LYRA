# import socket
import subprocess
import Modules.audio_ui as audio_ui
import os

RED_CROSS8_IP = "81.92.80.56"
def emergency_resources_reachable():
    hostname = RED_CROSS8_IP # example
    response = os.system("ping " + hostname)

    # and then check the response...
    if response == 0:
        return True
    else:
        return False

def process(data):
    if emergency_resources_reachable():
        print('hi')
        audio_ui.speak("Ressources d'urgence disponibles")
    print('')