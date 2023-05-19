import sys
from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QApplication
from PySide6 import QtGui
from PySide6.QtCore import QThread

from chatMain import Ui_chat_main

class chatting(QThread):
    def __init__(self):
        super(chatting, self).__init__()

class mainFile(QWidget):
    def __init__(self):
        super(mainFile, self).__init__()
        print("Main FILE")
        self.chatUI = Ui_chat_main()
        self.chatUI.setupUi(self)
        self.chatUI.pushButton.clicked.connect(self.sendText)

    def sendText(self):
        cmd = self.chatUI.lineEdit.text()
        if cmd:
            self.chatUI.lineEdit.clear()
            cmd2 = self.chatUI.plainTextEdit.toPlainText()
            if  cmd2 == "":
                self.chatUI.plainTextEdit.appendPlainText(f"{cmd}")
            else:
                self.chatUI.plainTextEdit_2.appendPlainText(f"{cmd}")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = mainFile()
    ui.show()
    sys.exit(app.exec())