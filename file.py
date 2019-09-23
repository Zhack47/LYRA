import Modules.utils as ut
import time
from Modules.identification import username
import Modules.emergency as emergency
import Modules.audio_ui as audio_ui
import Modules.IOverify as IO
import Modules.translate as trans

# This function is the main processing function, it treats a string, and directs it to another function
# depending on what is in it. It does not return anything (yet)


def file(data):
    data = IO.treat_intent("Océane", data)
    if "comment vas-tu" in data:
        audio_ui.speak("je vais bien, merci")

    if "quelle heure est il?" in data:
        audio_ui.speak(ut.return_current_time())

    if "où est" in data:
        ut.find_location(data)

    if "mode urgence" in data:
        emergency.process(data)


    for string in ["traduis", "traduit", "traduire"]:
        found_string = None
        if string in data:
            found_string = string
            print(found_string)
            break


    if not (found_string is None):
        data = IO.treat_intent(found_string, data)

        if not (len(data) < 3):
            try:
                res = trans.translate_data(data)
            except:
                res = ('désolé, je n''ai pas compris votre demande', 'fr')
            audio_ui.speak(res, trans.tr(res))
        else:
            audio_ui.speak("Que voulez vous que je traduise?", 'fr')

# initialization
time.sleep(2)
audio_ui.speak("Bonjour " + username + ", que puis-je faire pour vous?", 'fr')

while 1:
    data = audio_ui.recordAudio()
    data = data.split(" ")
    if "Océane" in data:
        file(data)
    else:
        with open("audiorec.txt", "w") as text_file:
            print("{}".format(data), file=text_file)



