from cx_Freeze import setup, Executable
import sys


includes = []
excludes = []
#"Modules.utils", "Modules.audio_ui", "Modules.emergency", "Modules.identification", "Modules.IOverify", "Modules.lang_dict", "Modules.translate",
packages = ["time", "os", "speech_recognition", "gtts", "googletrans"]  # nommer les packages utilises

if sys.platform == "win32":
    pass
    # includefiles += [...] : ajouter les recopies specifiques à Windows
elif sys.platform == "linux2":
    pass
    # includefiles += [...] : ajouter les recopies specifiques à Linux
else:
    pass
    # includefiles += [...] : cas du Mac OSX non traite ici

# pour que les bibliotheques binaires de /usr/lib soient recopiees aussi sous Linux
binpathincludes = []
if sys.platform == "linux2":
    binpathincludes += ["/usr/lib"]

# niveau d'optimisation pour la compilation en bytecodes
optimize = 0

# si True, n'affiche que les warning et les erreurs pendant le traitement cx_freeze
silent = True

options = {"includes": includes,
           "excludes": excludes,
           "packages": packages,
           "bin_path_includes": binpathincludes,
           "optimize": optimize,
           "silent": silent
           }

if sys.platform == "win32":
    options["include_msvcr"] = True

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # pour application graphique sous Windows
    # base = "Console" # pour application en console sous Windows

cible_2 = Executable(
    script="file.py",
    base=base,
    )

setup(
    name = "salut",
    version = "0.0.1",
    description = "file",
    options={"build_exe": options},
    executables = [cible_2]
)