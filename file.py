import Modules.utils as ut
import time
from Modules.identification import username
import Modules.emergency as emergency
import Modules.audio_ui as audio_ui
import Modules.IOverify as IO


# This function is the main processing function, it treats a string, and directs it to another function
# depending on what is in it. It does not return anything (yet)
def file(data):
    data = IO.recognize_intent("Lyra", data)
    if "comment vas-tu" in data:
        audio_ui.speak("je vais bien, merci")

    if "quelle heure est il?" in data:
        audio_ui.speak(ut.return_current_time())

    if "où est" in data:
        ut.find_location(data)

    if "mode urgence" in data:
        emergency.process(data)


# initialization
time.sleep(2)
audio_ui.speak("Bonjour "+ username + ", que puis-je faire pour vous?")

while 1:
    data = audio_ui.recordAudio()
    if "Lyra" in data:
        IO.recognize_intent("Lyra", data)
        file(data)
    else:
        with open("audiorec.txt", "w") as text_file:
            print("{}".format(data), file=text_file)
