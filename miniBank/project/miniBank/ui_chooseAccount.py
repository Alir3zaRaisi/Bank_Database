# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chooseAccount.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2 import QtWidgets
from ui_userMainMenu import Ui_userMainMenu

class Ui_chooseAccount(object):
    def setupUi(self, chooseAccount):
        if not chooseAccount.objectName():
            chooseAccount.setObjectName(u"chooseAccount")
        chooseAccount.resize(400, 300)
        self.choose_account_cmb = QComboBox(chooseAccount)
        self.choose_account_cmb.setObjectName(u"choose_account_cmb")
        self.choose_account_cmb.setGeometry(QRect(60, 160, 191, 41))
        self.choose_account_lbl = QLabel(chooseAccount)
        self.choose_account_lbl.setObjectName(u"choose_account_lbl")
        self.choose_account_lbl.setGeometry(QRect(60, 110, 281, 31))
        self.welcome_lbl = QLabel(chooseAccount)
        self.welcome_lbl.setObjectName(u"welcome_lbl")
        self.welcome_lbl.setGeometry(QRect(60, 50, 81, 16))
        self.OK_pbn = QPushButton(chooseAccount)
        self.OK_pbn.setObjectName(u"OK_pbn")
        self.OK_pbn.setGeometry(QRect(280, 240, 93, 28))

        #connect
        self.OK_pbn.clicked.connect(self.accountChosen)

        self.retranslateUi(chooseAccount)

        QMetaObject.connectSlotsByName(chooseAccount)
    # setupUi

    def retranslateUi(self, chooseAccount):
        chooseAccount.setWindowTitle(QCoreApplication.translate("chooseAccount", u"Form", None))
        self.choose_account_lbl.setText(QCoreApplication.translate("chooseAccount", u"please choose your preferred account:", None))
        self.welcome_lbl.setText(QCoreApplication.translate("chooseAccount", u"welcome", None))
        self.OK_pbn.setText(QCoreApplication.translate("chooseAccount", u"OK", None))
    # retranslateUi

    @Slot()
    def accountChosen(self):
        self.ex = Ui_userMainMenu()
        self.w = QtWidgets.QWidget()
        self.ex.setupUi(self.w)
        self.w.show()

        # refresh ui
        self.ex.retranslateUi

        self.w.show()
