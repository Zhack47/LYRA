# Ok, so this one is a bit confuse still. I think that most of this module will be directed to establish a "code"
# for the user/machine communication


def recognize_intent(word, data): # recognizes "word" in "data"
    if word in data:
        return True
    return False


def treat_intent(word, data):  # reduces the input to only the intent (what comes after 'word')
    if recognize_intent(word, data):
        for i in range(len(data)):
            if data[i] == word:
                intent_cut_index = i+1
                data = data[intent_cut_index:]
                return data
    print('intent error')
    return None
