# This module treats audio data, it can "hear", recognize, and speak. I did none of that, I should copy paste credits one day
import speech_recognition as sr
import os
from gtts import gTTS


def speak(audioString, lang):
    save_audio(audioString, lang)
    const = "mpg123 audio.mp3"
    print(audioString)
    os.system(const)


def listenToMe():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("En écoute!")
        audio = r.listen(source)
    return audio
def recordAudio():
    r = sr.Recognizer()
    audio = listenToMe()
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

def save_audio(audioString, lang):
    tts = gTTS(text=audioString, lang=lang)
    tts.save("audio.mp3")
