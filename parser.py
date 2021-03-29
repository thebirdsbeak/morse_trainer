from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from morsify import MorseUtilities as m
from random import randrange, choice
import parserui
import toolkitui

# TO DO:
#   Add more line templates
#   Add easy / med / hard (e.g. repeat callsign
#   Add choice of wpm
#   Use fun images to show success / failure

class ParserViewer(QtWidgets.QMainWindow, parserui.Ui_MainWindow):

    ### Setup ###
    def __init__(self, parent=toolkitui.Ui_MainWindow):
        ''' initaliser for bookshelf view '''
        super(ParserViewer, self).__init__(parent)
        self.setupUi(self)

        self.parserstartButton.clicked.connect(self.quizhandler)
        self.parserrepeatButton.clicked.connect(self.repeat_question)
        self.parserenterButton.clicked.connect(self.validate_entry)

        #Call Variables
        self.qsocall = ""
        self.rst = ""
        self.qth = ""
        self.name = ""
        self.question = ""

    def quizhandler(self):
        self.quiz_callsign()
        self.quiz_rst()
        self.quiz_qth()
        self.quiz_name()
        self.line_template()
        print("~~~~~")
        print(self.question)
        print("~~~~~")
        m.make_beep(self.question)

    def quiz_callsign(self):
        de = m.callsign()
        self.qsocall = de

    def quiz_rst(self):
        weightlist = ["duck", "duck",
                      "duck", "duck",
                      "duck", "dog",
                      "dog", "dog",
                      "dog", "cat",
                      "cat"]
        weighted = choice(weightlist)
        if weighted == "duck":
            self.rst = "NN"
        elif weighted == "dog":
            self.rst = "599"
        elif weighted == "cat":
            read = str(randrange(1, 5))
            sign = str(randrange(1, 9))
            stren = str(randrange(1, 9))
            rstring = read + sign + stren
            self.rst = rstring

    def quiz_qth(self):
        locations = ["Falkirk", "Livingston",
                     "Glasgow", "Edinburgh",
                     "Liverpool", "Stirling",
                     "Manchester", "St Andrews",
                     "London", "Fife"]
        loc = choice(locations)
        self.qth = loc

    def quiz_name(self):
        names = ["James", "John",
                 "Robert", "Michael",
                 "William", "David",
                 "Craig", "Ross",
                 "Donald", "Mark",
                 "Mary", "Gemma",
                 "Nancy", "Sarah",
                 "Ashley", "Sandra",
                 "Gillian", "Bob",
                 "Bill", "Jill",
                 "Fox", "Dana"]
        name = choice(names)
        self.name = name

    def line_template(self):
        c = self.qsocall
        n = self.name
        q = self.qth
        r = self.rst
        t = f"2M0KRG DE {c} UR {r} = TNX FER CALL = NAME IS {n}, QTH IS {q} = QTH? DE {c} K"
        self.question = t
        
    def keyPressEvent(self, e):
        ''' Keypress events to close window '''
        if e.key() == QtCore.Qt.Key_Escape:
            self.hide()
        if e.key() == QtCore.Qt.Key_R:
            self.repeat_question()

    def validate_entry(self):
        callguess = self.callEdit.text().upper()
        if callguess == self.qsocall.upper():
            print("Callsign correct!")
        else:
            print("Callsign incorrect")
        rstguess = self.rstEdit.text().upper()
        if rstguess == self.rst.upper():
            print("RST correct!")
        else:
            print("RST incorrect")
        nameguess = self.nameEdit.text().upper()
        if nameguess == self.name.upper():
            print("Name correct!")
        else:
            print("Name incorrect")
        qthguess = self.qthEdit.text().upper()
        if qthguess == self.qth.upper():
            print("QTH correct!")
        else:
            print("QTH incorrect")

    def repeat_question(self):
        m.make_beep(self.question)

    def close_parser(self):
        ''' Closes parser window '''
        self.hide()
