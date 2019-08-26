from googletrans import Translator
import Modules.audio_ui as audio_ui
def from_audio_translate_to_str(Audiostr, target_lang):
    translator = Translator()
    language = translator.detect(Audiostr).lang
    strin = translator.translate(Audiostr, src=language, dest=target_lang).text
    strin = str(strin)
    audio_ui.speak(strin)
    return strin
