# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signUp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui_signUpResult import Ui_signUpResult
from PySide2 import QtWidgets



class Ui_signUp(object):
    def setupUi(self, signUp):
        if not signUp.objectName():
            signUp.setObjectName(u"signUp")
        signUp.resize(400, 300)
        self.formLayoutWidget = QWidget(signUp)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(110, 120, 191, 123))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.username_lbl = QLabel(self.formLayoutWidget)
        self.username_lbl.setObjectName(u"username_lbl")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.username_lbl)

        self.password_lbl = QLabel(self.formLayoutWidget)
        self.password_lbl.setObjectName(u"password_lbl")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.password_lbl)

        self.accountNumber_lbl = QLabel(self.formLayoutWidget)
        self.accountNumber_lbl.setObjectName(u"accountNumber_lbl")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.accountNumber_lbl)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.formLayout.setItem(3, QFormLayout.LabelRole, self.horizontalSpacer)

        self.signUp_pbn = QPushButton(self.formLayoutWidget)
        self.signUp_pbn.setObjectName(u"signUp_pbn")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.signUp_pbn)

        self.username_led = QLineEdit(self.formLayoutWidget)
        self.username_led.setObjectName(u"username_led")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.username_led)

        self.password_led = QLineEdit(self.formLayoutWidget)
        self.password_led.setObjectName(u"password_led")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.password_led)

        self.accountNumber_led = QLineEdit(self.formLayoutWidget)
        self.accountNumber_led.setObjectName(u"accountNumber_led")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.accountNumber_led)

        #connect
        self.signUp_pbn.clicked.connect(self.createNewUser)

        self.retranslateUi(signUp)

        QMetaObject.connectSlotsByName(signUp)
    # setupUi

    def retranslateUi(self, signUp):
        signUp.setWindowTitle(QCoreApplication.translate("signUp", u"Form", None))
        self.username_lbl.setText(QCoreApplication.translate("signUp", u"username", None))
        self.password_lbl.setText(QCoreApplication.translate("signUp", u"password", None))
        self.accountNumber_lbl.setText(QCoreApplication.translate("signUp", u"accountNumber", None))
        self.signUp_pbn.setText(QCoreApplication.translate("signUp", u"sign up!", None))
    # retranslateUi

    @Slot()
    def createNewUser(self):
        #alireza
        #store new users data

        self.ex = Ui_signUpResult()
        self.w = QtWidgets.QWidget()
        self.ex.setupUi(self.w)
        self.w.show()

        # refresh ui
        self.ex.retranslateUi
        self.w.show()
