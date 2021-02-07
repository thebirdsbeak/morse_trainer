from PyQt5 import QtCore, QtWidgets
import simulatedui
import toolkitui
from morsify import MorseUtilities as m
from random import choice


class SimulatedViewer(QtWidgets.QMainWindow, simulatedui.Ui_MainWindow):

    def __init__(self, parent=toolkitui.Ui_MainWindow):
        """initaliser for bookshelf view"""
        super(SimulatedViewer, self).__init__(parent)
        self.setupUi(self)
        self.get_call()

        self.simulatedrepeatButton.clicked.connect(self.repeat_qso)
        self.simulatedstartButton.clicked.connect(self.contest)
        self.callsignButton.clicked.connect(self.update_call)
        self.simulatedEdit.returnPressed.connect(self.simulated_input_handler)

        self.qso_state = 0
        self.my_call = ""
        self.qso_call = ""
        self.memory_bank = ""
        self.listening = False
        self.remove_list = ["AR", "K", "BK", "FER", "FR"
                            "CALL", "RR", "THX", "TNX"]

    def keyPressEvent(self, e):
        """Keypress events to close window"""
        if e.key() == QtCore.Qt.Key_Escape:
            self.hide()
        if e.key() == QtCore.Qt.Key_R:
            self.repeat_qso()
        if e.key() == QtCore.Qt.Key_L:
            self.toggle_listen()

    def close_simulated(self):
        """Closes simulator window"""
        self.hide()

    def toggle_listen(self):
        if self.listening is False:
            self.listening = True
            self.simulatedstartButton.setStyleSheet("background-color: green")
            self.contest()
        else:
            self.listening = False
            self.simulatedstartButton.setStyleSheet("background-color: none")

    def get_call(self):
        """Fetches  callsign from text file"""
        with open("callsign.txt", "r") as callfile:
            callsign = callfile.readlines()
            call = callsign[0].strip()
        self.callsignLabel.setText(call)
        self.my_call = call

    def update_call(self):
        new_call = self.simulatedEdit.text().upper()
        if new_call != "":
            clean_call = new_call.split()[0]
            self.callsignLabel.setText(clean_call)
            with open("callsign.txt", "w") as callfile:
                callfile.write(clean_call)
            self.simulatedEdit.clear()
            self.my_call = clean_call

    def repeat_qso(self):
        """Repeats memory bank"""
        de = self.memory_bank
        m.make_beep(de)

    def toggle_qsolisten(self):
        """Toggles listen button on Simulated QSP"""
        if self.listening is False:
            self.listening = True
            self.simulatedstartButton.setStyleSheet("background-color: green")
            self.contest()
        else:
            self.listening = False
            self.simulatedstartButton.setStyleSheet("background-color: none")

    def clearqsos(self):
        """Simply clears qso browser"""
        self.simulatedBrowser.clear()

    def simulated_input_handler(self):
        """Handles current progress through qso"""
        if self.qso_state == 1:
            self.first_reply()
        elif self.qso_state == 2:
            self.second_reply()
        else:
            return

    def contest(self):
        """Initial contest cq call"""
        de = m.callsign()
        self.qso_call = de
        cq_call = f"CQ CQ CQ DE {de} AR K"
        self.simulatedBrowser.append(cq_call)
        m.make_beep(cq_call)
        self.qso_state = 1

    def clean_qsostring(self, qso_string):
        """Removes whitespace and watch words from reply"""
        raw_words = qso_string.split()
        clean_words = list(dict.fromkeys(raw_words))
        for i in clean_words:
            if i in self.remove_list:
                clean_words.remove(i)
        return clean_words

    def first_reply(self):
        self.my_call = self.callsignLabel.text()
        qso_string = self.simulatedEdit.text().upper()
        clean_words = self.clean_qsostring(qso_string)
        answer = f"{self.qso_call} DE {self.my_call}"
        if " ".join(clean_words) == answer:
            reply_styled = f"<span style=\"color:green;\" >{qso_string}</span>"
            self.simulatedBrowser.append(reply_styled)
            self.simulatedEdit.clear()
            self.qso_state = 2
            reply_line = f"{self.my_call} DE {self.qso_call} UR 599 K"
            self.simulatedBrowser.append(reply_line)
            m.make_beep(reply_line)
        elif self.my_call in clean_words:
            self.repeat_qso_call()
        elif self.qso_call in clean_words:
            self.repeat_my_call()
        else:
            error_line = f"SRI {self.qso_call}"
            self.simulatedBrowser.append(error_line)
            m.make_beep(error_line)
            self.contest()

    def repeat_qso_call(self):
        tx_call = self.qso_call
        repeat_calls = [f"N {tx_call} {tx_call} K",
                        f"N DE {tx_call} AGN {tx_call} HW?",
                        f"ZWF {tx_call} {tx_call} CFM?",
                        f"ZWF {tx_call} K"]
        rpt = choice(repeat_calls)
        self.simulatedBrowser.append(rpt)
        m.make_beep(rpt)

    def repeat_my_call(self):
        tx_call = self.qso_call
        repeat_calls = [f"{tx_call} PSE RPT? K",
                        f"{tx_call} QRZ?",
                        f"{tx_call} SRI PSE RPT? K",
                        f"{tx_call} PSE RPT QRZ"]
        rpt = choice(repeat_calls)
        self.simulatedBrowser.append(rpt)
        m.make_beep(rpt)

    def request_rst(self):
        tx_call = self.qso_call
        rx_call = self.my_call
        rpt = f"{rx_call} de {tx_call} RST?"
        self.simulatedBrowser.append(rpt)
        m.make_beep(rpt)

    def called_cq(self):
        '''Function where enter pressed on cq tab not in listen mode'''
        return
