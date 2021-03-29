from playsound import playsound
from random import choice

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H",
            "I", "J", "K", "L", "M", "N", "O", "P",
            "Q", "R", "S", "T", "U", "V", "W", "X",
            "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
prefixes =["M2", "M6", "2M0", "G1", "G2", "G3",
           "G4", "G5", "G6", "G7", "M1", "M3", "M0"]
punctuation = [".", ",", "?", "="]


class MorseUtilities():

    def __init__(self):
        return

    def callsign():
        prefix = choice(prefixes)
        suffix = ""
        for i in range(3):
            suffix += choice(alphabet)
        contact = prefix + suffix
        return contact

    def make_beep(beepstring):
        '''Turns a string in to morse beeps'''
        sound_base = 'twenty/{}.wav'
        for i in beepstring:
            if i == " ":
                playsound('twenty/SPACE.wav')
            elif i == ".":
                playsound('twenty/STOP.wav')
                playsound('twenty/UNITS.wav')
            elif i == ",":
                playsound('twenty/COMMA.wav')
                playsound('twenty/UNITS.wav')
            elif i == "?":
                playsound('twenty/QUESTION.wav')
                playsound('twenty/UNITS.wav')
            elif i == "=":
                playsound('twenty/EQUALS.wav')
                playsound('twenty/UNITS.wav')
            else:
                x = i.upper()
                if x in alphabet or x in numbers:
                    active_sound = sound_base.format(x)
                    playsound(active_sound)
                    playsound('twenty/UNITS.wav')
                else:
                    return
