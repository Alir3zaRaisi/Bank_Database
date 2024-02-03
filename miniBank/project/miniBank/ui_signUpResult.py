# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signUpResult.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_signUpResult(object):
    def setupUi(self, signUpResult):
        if not signUpResult.objectName():
            signUpResult.setObjectName(u"signUpResult")
        signUpResult.resize(400, 300)
        self.sign_up_complete_lbl = QLabel(signUpResult)
        self.sign_up_complete_lbl.setObjectName(u"sign_up_complete_lbl")
        self.sign_up_complete_lbl.setGeometry(QRect(30, 80, 211, 51))
        self.close_pbn = QPushButton(signUpResult)
        self.close_pbn.setObjectName(u"close_pbn")
        self.close_pbn.setGeometry(QRect(190, 210, 93, 28))

        self.retranslateUi(signUpResult)
        self.close_pbn.clicked.connect(signUpResult.close)

        QMetaObject.connectSlotsByName(signUpResult)
    # setupUi

    def retranslateUi(self, signUpResult):
        signUpResult.setWindowTitle(QCoreApplication.translate("signUpResult", u"Form", None))
        self.sign_up_complete_lbl.setText(QCoreApplication.translate("signUpResult", u"sign up complete!", None))
        self.close_pbn.setText(QCoreApplication.translate("signUpResult", u"close", None))
    # retranslateUi

