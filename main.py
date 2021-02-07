from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import os
import toolkitui
from kochtrainer import KochViewer
from simulated import SimulatedViewer
from parser import ParserViewer
from practice import PracticeViewer
from morsify import MorseUtilities as m

class MainDialog(QtWidgets.QMainWindow, toolkitui.Ui_MainWindow):

    # Setup #
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

        self.kochButton.clicked.connect(self.openKoch)
        self.quizButton.clicked.connect(self.openQuiz)
        self.practiceButton.clicked.connect(self.openPractice)
        self.simulatedButton.clicked.connect(self.openSimulated)

        self.koch = KochViewer(self)
        self.sim = SimulatedViewer(self)
        self.quiz = ParserViewer(self)
        self.prac = PracticeViewer(self)

    def keyPressEvent(self, e):
        ''' Keypress events to close window '''
        if e.key() == QtCore.Qt.Key_Escape:
            self.hide()
        elif e.key() == QtCore.Qt.Key_K:
            self.openKoch()
        elif e.key() == QtCore.Qt.Key_P:
            self.openPractice()
        elif e.key() == QtCore.Qt.Key_S:
            self.openSimulated()
        elif e.key() == QtCore.Qt.Key_Q:
            self.openQuiz

    def openKoch(self):
        """Opens Koch Trainer"""
        self.koch.show()

    def openQuiz(self):
        """Opens Quiz Mode (Parser)"""
        self.quiz.show()

    def openPractice(self):
        """Opens Practice Mode"""
        self.prac.show()

    def openSimulated(self):
        """Opens Simulated Mode"""
        
        self.sim.show()

app = QtWidgets.QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()


    
