# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parserui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(601, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.parserBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.parserBrowser.setObjectName("parserBrowser")
        self.gridLayout.addWidget(self.parserBrowser, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 4, 0, 1, 1)
        self.parserrepeatButton = QtWidgets.QPushButton(self.centralwidget)
        self.parserrepeatButton.setObjectName("parserrepeatButton")
        self.gridLayout_3.addWidget(self.parserrepeatButton, 2, 5, 1, 1)
        self.callEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.callEdit.setObjectName("callEdit")
        self.gridLayout_3.addWidget(self.callEdit, 1, 2, 1, 1)
        self.rstEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.rstEdit.setObjectName("rstEdit")
        self.gridLayout_3.addWidget(self.rstEdit, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)
        self.parserstartButton = QtWidgets.QPushButton(self.centralwidget)
        self.parserstartButton.setObjectName("parserstartButton")
        self.gridLayout_3.addWidget(self.parserstartButton, 1, 5, 1, 1)
        self.answerEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.answerEdit.setObjectName("answerEdit")
        self.gridLayout_3.addWidget(self.answerEdit, 4, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 3, 2, 1, 1)
        self.parserrestartButton = QtWidgets.QPushButton(self.centralwidget)
        self.parserrestartButton.setObjectName("parserrestartButton")
        self.gridLayout_3.addWidget(self.parserrestartButton, 3, 5, 1, 1)
        self.scoreLabel = QtWidgets.QLabel(self.centralwidget)
        self.scoreLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.scoreLabel.setObjectName("scoreLabel")
        self.gridLayout_3.addWidget(self.scoreLabel, 4, 5, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 601, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QSO Parser"))
        self.label.setText(_translate("MainWindow", "RST:"))
        self.label_2.setText(_translate("MainWindow", "Answer:"))
        self.parserrepeatButton.setText(_translate("MainWindow", "Repeat"))
        self.label_4.setText(_translate("MainWindow", "Question:"))
        self.parserstartButton.setText(_translate("MainWindow", "Start"))
        self.label_3.setText(_translate("MainWindow", "Callsign:"))
        self.label_5.setText(_translate("MainWindow", "Question will appear here"))
        self.parserrestartButton.setText(_translate("MainWindow", "Restart"))
        self.scoreLabel.setText(_translate("MainWindow", "0 / 10"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
