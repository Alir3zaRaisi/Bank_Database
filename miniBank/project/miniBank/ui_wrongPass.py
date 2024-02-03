# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wrongPass.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_wrongPass(object):
    def setupUi(self, wrongPass):
        if not wrongPass.objectName():
            wrongPass.setObjectName(u"wrongPass")
        wrongPass.setWindowModality(Qt.WindowModal)
        wrongPass.resize(400, 300)
        self.verticalLayoutWidget = QWidget(wrongPass)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 100, 261, 80))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.wrong_lbl = QLabel(self.verticalLayoutWidget)
        self.wrong_lbl.setObjectName(u"wrong_lbl")

        self.verticalLayout.addWidget(self.wrong_lbl)

        self.try_again_lbl = QLabel(self.verticalLayoutWidget)
        self.try_again_lbl.setObjectName(u"try_again_lbl")

        self.verticalLayout.addWidget(self.try_again_lbl)

        self.ok_pbn = QPushButton(wrongPass)
        self.ok_pbn.setObjectName(u"ok_pbn")
        self.ok_pbn.setGeometry(QRect(240, 240, 93, 28))

        self.retranslateUi(wrongPass)
        self.ok_pbn.clicked.connect(wrongPass.close)

        QMetaObject.connectSlotsByName(wrongPass)
    # setupUi

    def retranslateUi(self, wrongPass):
        wrongPass.setWindowTitle(QCoreApplication.translate("wrongPass", u"Form", None))
        self.wrong_lbl.setText(QCoreApplication.translate("wrongPass", u"username or password is wrong!", None))
        self.try_again_lbl.setText(QCoreApplication.translate("wrongPass", u"please try again.", None))
        self.ok_pbn.setText(QCoreApplication.translate("wrongPass", u"OK", None))
    # retranslateUi

