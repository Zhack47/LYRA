from googletrans import Translator
import Modules.audio_ui as audio_ui
import Modules.IOverify as IO
translator = Translator()
def from_audio_translate_to_str(Audiostr, target_lang):
    language = translator.detect(Audiostr).lang
    strin = translator.translate(Audiostr, src=language, dest=target_lang).text
    strin = str(strin)
    audio_ui.speak(strin)
    return strin


def translate_data(data):
    target_lang = acknowledge_output_language(data)
    if target_lang == None:
        return from_audio_translate_to_str(data, 'fr')
    else:
        return from_audio_translate_to_str(data, target_lang)


def acknowledge_output_language(data):
    if "en" in data:
        data = IO.treat_intent('en', data)
        return data[1]
    return None