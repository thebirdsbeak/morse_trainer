from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import kochtrainerui
import toolkitui
from random import choice
from morsify import MorseUtilities as m
from morsify import alphabet, numbers
from playsound import playsound


class KochViewer(QtWidgets.QMainWindow, kochtrainerui.Ui_MainWindow):

    ### Setup ###
    def __init__(self, parent=toolkitui.Ui_MainWindow):
        ''' initaliser for bookshelf view '''
        super(KochViewer, self).__init__(parent)
        self.setupUi(self)

        self.active_letters = []
        self.listening = False
        self.memory_bank = []
        self.counter = 0

        self.kochstartButton.clicked.connect(self.toggle_listen)
        self.kochEdit.textEdited.connect(self.edit_hander)
        self.pushButton.clicked.connect(self.repeat_koch)
        self.comboBox.currentTextChanged.connect(self.change_mode)

        self.checklist = [(self.aCheck, "A"), (self.bCheck, "B"),
                          (self.cCheck, "C"), (self.dCheck, "D"),
                          (self.eCheck, "E"), (self.fCheck, "F"),
                          (self.gCheck, "G"), (self.hCheck, "H"),
                          (self.iCheck, "I"), (self.jCheck, "J"),
                          (self.kCheck, "K"), (self.lCheck, "L"),
                          (self.mCheck, "M"), (self.nCheck, "N"),
                          (self.oCheck, "O"), (self.pCheck, "P"),
                          (self.qCheck, "Q"), (self.rCheck, "R"),
                          (self.sCheck, "S"), (self.tCheck, "T"),
                          (self.uCheck, "U"), (self.vCheck, "V"),
                          (self.wCheck, "W"), (self.xCheck, "X"),
                          (self.yCheck, "Y"), (self.zCheck, "Z"),
                          (self.oneCheck, "1"), (self.twoCheck, "2"),
                          (self.thrCheck, "3"), (self.fouCheck, "4"),
                          (self.fivCheck, "5"), (self.sixCheck, "6"),
                          (self.sevCheck, "7"), (self.eigCheck, "8"),
                          (self.ninCheck, "9"), (self.zerCheck, "0"),
                          (self.periodCheck, "."), (self.commaCheck, ","),
                          (self.questionCheck, "?"), (self.equalsCheck, "=")]

        self.barlist = [[self.aBar, 0], [self.bBar, 0], [self.cBar, 0],
                        [self.dBar, 0], [self.eBar, 0], [self.fBar, 0],
                        [self.gBar, 0], [self.hBar, 0], [self.iBar, 0],
                        [self.jBar, 0], [self.kBar, 0], [self.lBar, 0],
                        [self.mBar, 0], [self.nBar, 0], [self.oBar, 0],
                        [self.pBar, 0], [self.qBar, 0], [self.rBar, 0],
                        [self.sBar, 0], [self.tBar, 0], [self.uBar, 0],
                        [self.vBar, 0], [self.wBar, 0], [self.xBar, 0],
                        [self.yBar, 0], [self.zBar, 0], [self.oneBar, 0],
                        [self.twoBar, 0], [self.thrBar, 0], [self.fouBar, 0],
                        [self.fivBar, 0], [self.sixBar, 0], [self.sevBar, 0],
                        [self.eigBar, 0], [self.ninBar, 0], [self.zerBar, 0],
                        [self.periodBar, 0], [self.commaBar, 0],
                        [self.questionBar, 0], [self.equalsBar, 0]]

    def keyPressEvent(self, e):
        ''' Keypress events to close window '''
        if e.key() == QtCore.Qt.Key_Escape:
            self.hide()
        elif e.key() == QtCore.Qt.Key_R:
            self.repeat_koch()
        elif e.key() == QtCore.Qt.Key_L:
            self.toggle_listen()
            
    def close_kochtrainer(self):
        ''' Closes bookshelf window '''
        self.hide()

    def edit_hander(self):
        if self.listening is True:
            self.check_input()
        else:
            return

    def repeat_koch(self):
        if self.memory_bank:
            de = self.memory_bank[0]
            m.make_beep(de)

    def toggle_listen(self):
        """Listen Button Toggled"""
        if self.listening is False:
            self.listening = True
            self.kochstartButton.setStyleSheet("background-color: green")
            self.kochEdit.setFocus()
            self.play_beeps()
        else:
            self.listening = False
            self.kochstartButton.setStyleSheet("background-color: none")
        
    def check_input(self):
        '''Checks entered call against generated callsign'''
        answer = str(self.kochEdit.text()).upper()
        self.kochEdit.clear()
        current_bar = self.barlist[self.memory_bank[1]]
        if answer != self.memory_bank[0]:
            if current_bar[1] - 10 <= 0:
                current_bar[1] = 0
            else:
                current_bar[1] = current_bar[1] - 10
            current_bar[0].setValue(current_bar[1])
            playsound("twenty/ERROR.wav")
            playsound("twenty/UNITS.wav")
        else:
            if current_bar[1] + 10 >= 100:
                current_bar[1] = 100
            else:
                current_bar[1] += 10
            current_bar[0].setValue(current_bar[1])
        check = self.check_win()
        if check == "Won":
            self.winner_dialog()
            self.toggle_listen()
            for x in self.barlist:
                x[1] = 0
                x[0].setValue(0)
        else:
            self.play_beeps()

    def play_beeps(self):
        self.active_letters = []
        for i in self.checklist:
            if i[0].isChecked():
                self.active_letters.append([i[1], self.checklist.index(i)])
        self.memory_bank = choice(self.active_letters)
        m.make_beep(self.memory_bank[0])

    def change_mode(self):
        self.active_letters = []
        if self.comboBox.currentText() == "Custom":
            return
        elif self.comboBox.currentText() == "Dits":
            current_letters = ["E", "I", "S", "H", "5", "A",
                               "U", "V", "4", "R", "F", "3",
                               "L", "2", "W", "J", "P", "1"]
        elif self.comboBox.currentText() == "Dahs":
            current_letters = ["T", "M", "N", "O", "G", "K",
                               "D", "Q", "Z", "Y", "C", "X",
                               "B", "0", "9", "8", "7", "6"]
        elif self.comboBox.currentText() == "Everything":
            current_letters = alphabet + numbers + [".", ",", "?", "="]
        elif self.comboBox.currentText() == "Letters":
            current_letters = alphabet
        elif self.comboBox.currentText() == "Numbers":
            current_letters = numbers
        elif self.comboBox.currentText() == "Punctuation":
            current_letters = [".", ",", "?", "="]
        for i in self.checklist:
            if i[1] in current_letters:
                self.active_letters.append([i[1], self.checklist.index(i)])
                i[0].setChecked(True)
            else:
                i[0].setChecked(False)

    def check_win(self):
        """Checks for win conditions"""
        full_marks = 0
        actual_marks = 0
        for i in self.checklist:
            if i[0].isChecked() == True:
                full_marks += 100
                index = self.checklist.index(i)
                score = self.barlist[index][1]
                actual_marks += score
        if full_marks == actual_marks:
            return "Won"
        else:
            return

    def winner_dialog(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Winner Winner chicken dinner!")
        msg.setInformativeText("Try again with more letters.")
        msg.setWindowTitle("Well done!")
        msg.exec_()
        
