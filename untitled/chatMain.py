# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QWidget)
from PySide6 import QtWidgets

class Ui_chat_main(object):
    def setupUi(self, chat_main):
        if not chat_main.objectName():
            chat_main.setObjectName(u"chat_main")
        chat_main.resize(356, 600)
        self.label = QLabel(chat_main)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 5, 311, 41))
        self.label.setStyleSheet(u"font: 700 italic 24pt \"Times New Roman\";\n"
"color: rgb(0, 0, 0);")
        self.label.setAlignment(Qt.AlignCenter)
        self.plainTextEdit = QPlainTextEdit(chat_main)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(193, 499, 161, 31))
        self.plainTextEdit_2 = QPlainTextEdit(chat_main)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(0, 460, 161, 31))
        self.plainTextEdit_3 = QPlainTextEdit(chat_main)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setGeometry(QRect(190, 400, 161, 31))
        self.plainTextEdit_4 = QPlainTextEdit(chat_main)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setGeometry(QRect(0, 350, 161, 31))
        self.plainTextEdit_5 = QPlainTextEdit(chat_main)
        self.plainTextEdit_5.setObjectName(u"plainTextEdit_5")
        self.plainTextEdit_5.setGeometry(QRect(190, 300, 161, 31))
        self.plainTextEdit_6 = QPlainTextEdit(chat_main)
        self.plainTextEdit_6.setObjectName(u"plainTextEdit_6")
        self.plainTextEdit_6.setGeometry(QRect(0, 250, 161, 31))
        self.plainTextEdit_7 = QPlainTextEdit(chat_main)
        self.plainTextEdit_7.setObjectName(u"plainTextEdit_7")
        self.plainTextEdit_7.setGeometry(QRect(190, 200, 161, 31))
        self.plainTextEdit_8 = QPlainTextEdit(chat_main)
        self.plainTextEdit_8.setObjectName(u"plainTextEdit_8")
        self.plainTextEdit_8.setGeometry(QRect(0, 160, 161, 31))
        self.plainTextEdit_9 = QPlainTextEdit(chat_main)
        self.plainTextEdit_9.setObjectName(u"plainTextEdit_9")
        self.plainTextEdit_9.setGeometry(QRect(190, 110, 161, 31))
        self.label_3 = QLabel(chat_main)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 5, 51, 41))
        self.label_3.setPixmap(QPixmap(u"C:/Users/Tomura Shigaraki/Downloads/text.png"))
        self.label_3.setScaledContents(True)
        self.label_4 = QLabel(chat_main)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(278, 5, 61, 41))
        self.label_4.setPixmap(QPixmap(u"C:/Users/Tomura Shigaraki/Downloads/share.png"))
        self.label_4.setScaledContents(True)
        self.pushButton = QPushButton(chat_main)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(290, 560, 61, 41))
        self.pushButton.setStyleSheet(u"border-image: url(C:/Users/Tomura Shigaraki/Downloads/telegram.png);")
        self.lineEdit = QLineEdit(chat_main)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(0, 560, 281, 41))
        self.lineEdit.setStyleSheet(u"background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 20pt \"Times New Roman\";")

        self.retranslateUi(chat_main)

        QMetaObject.connectSlotsByName(chat_main)
    # setupUi

    def retranslateUi(self, chat_main):
        chat_main.setWindowTitle(QCoreApplication.translate("Chat Room", u"Chat Room", None))
        self.label.setText(QCoreApplication.translate("chat_main", u"TC_CHAT", None))
        self.label_3.setText("")
        self.label_4.setText("")
        self.pushButton.setText("")
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    chat_main = QtWidgets.QWidget()
    ui = Ui_chat_main()
    ui.setupUi(chat_main)
    chat_main.show()
    sys.exit(app.exec())
