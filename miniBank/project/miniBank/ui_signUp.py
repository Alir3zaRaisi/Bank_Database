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
        self.formLayoutWidget.setGeometry(QRect(100, 60, 191, 168))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.password_lbl = QLabel(self.formLayoutWidget)
        self.password_lbl.setObjectName(u"password_lbl")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.password_lbl)

        self.password_led = QLineEdit(self.formLayoutWidget)
        self.password_led.setObjectName(u"password_led")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.password_led)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.formLayout.setItem(6, QFormLayout.LabelRole, self.horizontalSpacer)

        self.signUp_pbn = QPushButton(self.formLayoutWidget)
        self.signUp_pbn.setObjectName(u"signUp_pbn")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.signUp_pbn)

        self.first_name_lbl = QLabel(self.formLayoutWidget)
        self.first_name_lbl.setObjectName(u"first_name_lbl")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.first_name_lbl)

        self.first_name_led = QLineEdit(self.formLayoutWidget)
        self.first_name_led.setObjectName(u"first_name_led")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.first_name_led)

        self.last_name_lbl = QLabel(self.formLayoutWidget)
        self.last_name_lbl.setObjectName(u"last_name_lbl")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.last_name_lbl)

        self.last_name_led = QLineEdit(self.formLayoutWidget)
        self.last_name_led.setObjectName(u"last_name_led")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.last_name_led)

        self.username_lbl = QLabel(self.formLayoutWidget)
        self.username_lbl.setObjectName(u"username_lbl")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.username_lbl)

        self.username_led = QLineEdit(self.formLayoutWidget)
        self.username_led.setObjectName(u"username_led")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.username_led)

        #connect
        self.signUp_pbn.clicked.connect(self.createNewUser)


        self.retranslateUi(signUp)

        QMetaObject.connectSlotsByName(signUp)
    # setupUi

    def retranslateUi(self, signUp):
        signUp.setWindowTitle(QCoreApplication.translate("signUp", u"Form", None))
        self.password_lbl.setText(QCoreApplication.translate("signUp", u"password", None))
        self.signUp_pbn.setText(QCoreApplication.translate("signUp", u"sign up!", None))
        self.first_name_lbl.setText(QCoreApplication.translate("signUp", u"firstname", None))
        self.last_name_lbl.setText(QCoreApplication.translate("signUp", u"lastname", None))
        self.username_lbl.setText(QCoreApplication.translate("signUp", u"username", None))
    # retranslateUi

    @Slot()
    def createNewUser(self):
        first_name = self.first_name_led.text()
        last_name = self.last_name_led.text()
        userName = self.username_led.text()
        password = self.password_led.text()
        print(first_name,last_name,userName,password)
        #alireza
        #store new users data



        self.ex = Ui_signUpResult()
        self.w = QtWidgets.QWidget()
        self.ex.setupUi(self.w)
        self.w.show()

        # refresh ui
        self.ex.retranslateUi
        self.w.show()
