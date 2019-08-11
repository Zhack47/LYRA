import speech_recognition as sr
import os
from gtts import gTTS



def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='fr')
    tts.save("audio.mp3")
    const = "mpg321 audio.mp3"
    os.system(const)

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("En écoute!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio, language='fr-FR')
        print("Vous avez dit: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition n'a pas pu décoder l'audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data
