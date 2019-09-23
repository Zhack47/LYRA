from googletrans import Translator
import Modules.audio_ui as audio_ui
import Modules.IOverify as IO
import Modules.lang_dict as switch_lang
translator = Translator()

def tr(data):
    data = " ".join(data)
    print(translator.detect(data).lang)
    return translator.detect(data).lang
def from_audio_translate_to_str(Audiostr, target_lang):
    Audiostr = " ".join(Audiostr)
    language = translator.detect(Audiostr).lang
    strin = translator.translate(Audiostr, src=language, dest=target_lang).text
    strin = str(strin)
    return strin


def translate_data(data):
    target_lang = switch_lang.get_lang_symbol(str(acknowledge_output_language(data)).capitalize())
    if target_lang == None:
        return from_audio_translate_to_str(data, 'fr')
    else:
        return from_audio_translate_to_str(data[2:], target_lang)


def acknowledge_output_language(data):
    if "en" in data:
        data = IO.treat_intent('en', data)
        return data[0]
<<<<<<< HEAD
    return None
=======
    return None
>>>>>>> d7c918f93b279ee006c0b5ed6ee777168ecc4ff2
