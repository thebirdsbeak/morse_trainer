from PyQt5 import QtCore, QtWidgets
import practiceui
import toolkitui
from random import choice
from playsound import playsound
from morsify import MorseUtilities as m
from morsify import alphabet, numbers, punctuation
from words import random_word

# TODO
# test len for auto inputting of words and codegroups?


class PracticeViewer(QtWidgets.QMainWindow, practiceui.Ui_MainWindow):

    ### Setup ###
    def __init__(self, parent=toolkitui.Ui_MainWindow):
        ''' initaliser for bookshelf view '''
        super(PracticeViewer, self).__init__(parent)
        self.setupUi(self)

        self.practiceEdit.returnPressed.connect(self.input_handler)
        self.practiceEdit.textEdited.connect(self.edit_handler)
        self.practicestartButton.clicked.connect(self.toggle_listen)
        self.practicerepeatButton.clicked.connect(self.repeat_call)
        self.selectionBox.currentTextChanged.connect(self.toggle_selection)

        self.listening = False
        self.memory_bank = ""

    def keyPressEvent(self, e):
        ''' Keypress events to close window '''
        if e.key() == QtCore.Qt.Key_Escape:
            self.hide()
        elif e.key() == QtCore.Qt.Key_R:
            self.repeat_call()
        elif e.key() == QtCore.Qt.Key_L:
            self.toggle_listen()

    def check_input(self):
        '''Checks entered call against generated callsign'''
        wrong_answer = "<span style=\"color:red;\" >{}</span>"
        right_answer = "<span style=\"color:green;\" >{}</span>"
        answer = str(self.practiceEdit.text()).upper()
        self.practiceEdit.clear()
        if answer.strip() == self.memory_bank.strip():
            ans1 = right_answer.format(self.memory_bank)
            ans2 = right_answer.format(answer)            
        else:
            ans1 = wrong_answer.format(self.memory_bank)
            ans2 = wrong_answer.format(answer)
            playsound("twenty/ERROR.wav")
            playsound("twenty/UNITS.wav")
        self.rxBrowser.append(ans1)
        if answer != "":
            self.txBrowser.append(ans2)
        else:
            self.txBrowser.append(" ")
        if self.listening is True:
            if self.selectionBox.currentText() == "Callsigns":
                self.call()
            elif self.selectionBox.currentText() == "Words":
                self.word()
            elif self.selectionBox.currentText() == "Alphabet":
                self.letters()
            elif self.selectionBox.currentText() == "Codegroups":
                self.codegroups()
            elif self.selectionBox.currentText() == "Punctuation":
                self.punctuations()
            elif self.selectionBox.currentText() == "Numbers":
                self.number()
            elif self.selectionBox.currentText() == "AlphaNumPun":
                self.alphanumpun()
        else:
            return

    def repeat_call(self):
        de = self.memory_bank
        m.make_beep(de)
      
    def close_practice(self):
        ''' Closes parser window '''
        self.hide()

    def input_handler(self):
        '''Handles hitting enter on the callsign lineEdit'''
        if self.listening is True:
            self.check_input()
        else:
            self.parrot()

    def edit_handler(self):
        '''If edited, does a thing'''
        no_enter_key = ["Alphabet",
                        "AlphaNumPun",
                        "Numbers",
                        "Punctuation"]
        for i in no_enter_key:
            if self.selectionBox.currentText() == i:
                if self.listening is True:
                    self.check_input()
                else:
                    self.parrot()

    def toggle_listen(self):
        if self.listening is False:
            self.listening = True
            self.practicestartButton.setStyleSheet("background-color: green")
            self.practiceEdit.setFocus()
            if self.selectionBox.currentText() == "Callsigns":
                self.call()
            elif self.selectionBox.currentText() == "Words":
                self.word()
            elif self.selectionBox.currentText() == "Alphabet":
                self.letters()
            elif self.selectionBox.currentText() == "Codegroups":
                self.codegroups()
            elif self.selectionBox.currentText() == "Punctuation":
                self.punctuations()
            elif self.selectionBox.currentText() == "Numbers":
                self.number()
            elif self.selectionBox.currentText() == "AlphaNumPun":
                self.alphanumpun()
        else:
            self.listening = False
            self.practicestartButton.setStyleSheet("Background-color: none")

    def toggle_selection(self):
        if self.listening is True:
            self.listening = False
            self.practicestartButton.setStyleSheet("Background-color: none")

    def clearcalls(self):
        self.rxBrowser.clear()
        self.txBrowser.clear()

    def word(self):
        word = random_word().upper()
        self.memory_bank = str(word)
        m.make_beep(word)
        
    def call(self):
        '''Grabs a new callsign and sends it'''
        de = m.callsign()
        self.memory_bank = de
        m.make_beep(de)

    def letters(self):
        '''Alphabet'''
        letter = choice(alphabet)
        self.memory_bank = letter
        m.make_beep(letter)

    def codegroups(self):
        '''Codegroups test'''
        alphanum = alphabet + numbers
        code_group = ""
        for i in range(2):
            for i in range(5):
                code_group += choice(alphanum)
            code_group += " "
        self.memory_bank = code_group
        m.make_beep(code_group)

    def punctuations(self):
        '''Punctuation test'''
        mark = choice(punctuation)
        self.memory_bank = mark
        m.make_beep(mark)

    def number(self):
        '''Numbers test'''
        num = choice(numbers)
        self.memory_bank = num
        m.make_beep(num)

    def alphanumpun(self):
        '''Alpha, numbers, and punctuation test'''
        alphanump = alphabet + numbers + punctuation
        selection = choice(alphanump)
        self.memory_bank = selection
        m.make_beep(selection)

    def parrot(self):
        '''Takes letter and emits it back in morse'''
        entered_text = str(self.practiceEdit.text())
        self.practiceEdit.clear()
        self.memory_bank = entered_text
        m.make_beep(entered_text)
