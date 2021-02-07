from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import parserui
import toolkitui

class ParserViewer(QtWidgets.QMainWindow, parserui.Ui_MainWindow):

    ### Setup ###
    def __init__(self, parent=toolkitui.Ui_MainWindow):
        ''' initaliser for bookshelf view '''
        super(ParserViewer, self).__init__(parent)
        self.setupUi(self)

    def keyPressEvent(self, e):
        ''' Keypress events to close window '''
        if e.key() == QtCore.Qt.Key_Escape:
            self.hide()

    def close_parser(self):
        ''' Closes parser window '''
        self.hide()
