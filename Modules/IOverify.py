# Ok, so this one is a bit confuse still. I think that most of this module will be directed to establish a "code"
# for the user/machine communication
def recognize_intent(word, data): # recognizes "word" in "data"
    res = ""
    data = data.split(" ")
    ACTIVATION_REQUIRED = False
    if 'Lyra' in data:
        j = 0
        for i in range(len(data)):
            if (data[i] == word):
                ACTIVATION_REQUIRED = True
            if ACTIVATION_REQUIRED:
                data = data[i:]
            res = "  ".join(data)
    return res