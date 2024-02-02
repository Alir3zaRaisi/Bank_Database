# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'userMainMenu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_userMainMenu(object):
    def setupUi(self, userMainMenu):
        if not userMainMenu.objectName():
            userMainMenu.setObjectName(u"userMainMenu")
        userMainMenu.resize(400, 300)
        self.choose_lbl = QLabel(userMainMenu)
        self.choose_lbl.setObjectName(u"choose_lbl")
        self.choose_lbl.setGeometry(QRect(10, 70, 261, 41))
        self.action_cmb = QComboBox(userMainMenu)
        self.action_cmb.addItem("")
        self.action_cmb.addItem("")
        self.action_cmb.addItem("")
        self.action_cmb.addItem("")
        self.action_cmb.addItem("")
        self.action_cmb.addItem("")
        self.action_cmb.addItem("")
        self.action_cmb.addItem("")
        self.action_cmb.addItem("")
        self.action_cmb.addItem("")
        self.action_cmb.setObjectName(u"action_cmb")
        self.action_cmb.setGeometry(QRect(20, 130, 73, 22))
        self.action_pbn = QPushButton(userMainMenu)
        self.action_pbn.setObjectName(u"action_pbn")
        self.action_pbn.setGeometry(QRect(40, 210, 93, 28))
        self.formLayoutWidget = QWidget(userMainMenu)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(210, 100, 190, 171))
        self.chosenAction_lyt = QFormLayout(self.formLayoutWidget)
        self.chosenAction_lyt.setObjectName(u"chosenAction_lyt")
        self.chosenAction_lyt.setContentsMargins(0, 0, 0, 0)
        self.new_password_lbl = QLabel(self.formLayoutWidget)
        self.new_password_lbl.setObjectName(u"new_password_lbl")
        self.new_password_lbl.setEnabled(False)

        self.chosenAction_lyt.setWidget(0, QFormLayout.LabelRole, self.new_password_lbl)

        self.new_password_led = QLineEdit(self.formLayoutWidget)
        self.new_password_led.setObjectName(u"new_password_led")
        self.new_password_led.setEnabled(False)

        self.chosenAction_lyt.setWidget(0, QFormLayout.FieldRole, self.new_password_led)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.chosenAction_lyt.setItem(2, QFormLayout.LabelRole, self.horizontalSpacer)

        self.action_done_pbn = QPushButton(self.formLayoutWidget)
        self.action_done_pbn.setObjectName(u"action_done_pbn")
        self.action_done_pbn.setEnabled(False)

        self.chosenAction_lyt.setWidget(2, QFormLayout.FieldRole, self.action_done_pbn)

        self.number_lbl = QLabel(self.formLayoutWidget)
        self.number_lbl.setObjectName(u"number_lbl")
        self.number_lbl.setEnabled(False)

        self.chosenAction_lyt.setWidget(1, QFormLayout.LabelRole, self.number_lbl)

        self.number_led = QLineEdit(self.formLayoutWidget)
        self.number_led.setObjectName(u"number_led")
        self.number_led.setEnabled(False)

        self.chosenAction_lyt.setWidget(1, QFormLayout.FieldRole, self.number_led)

        self.horizontalLayoutWidget = QWidget(userMainMenu)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 151, 61))
        self.balance_lyt = QHBoxLayout(self.horizontalLayoutWidget)
        self.balance_lyt.setObjectName(u"balance_lyt")
        self.balance_lyt.setContentsMargins(0, 0, 0, 0)
        self.const_lbl = QLabel(self.horizontalLayoutWidget)
        self.const_lbl.setObjectName(u"const_lbl")

        self.balance_lyt.addWidget(self.const_lbl)

        self.balance_lbl = QLabel(self.horizontalLayoutWidget)
        self.balance_lbl.setObjectName(u"balance_lbl")

        self.balance_lyt.addWidget(self.balance_lbl)


        self.retranslateUi(userMainMenu)

        QMetaObject.connectSlotsByName(userMainMenu)
    # setupUi

    def retranslateUi(self, userMainMenu):
        userMainMenu.setWindowTitle(QCoreApplication.translate("userMainMenu", u"Form", None))
        self.choose_lbl.setText(QCoreApplication.translate("userMainMenu", u"please click on one of the following options:", None))
        self.action_cmb.setItemText(0, QCoreApplication.translate("userMainMenu", u"change password", None))
        self.action_cmb.setItemText(1, QCoreApplication.translate("userMainMenu", u"recent transactions", None))
        self.action_cmb.setItemText(2, QCoreApplication.translate("userMainMenu", u"transactions - time based", None))
        self.action_cmb.setItemText(3, QCoreApplication.translate("userMainMenu", u"account's info", None))
        self.action_cmb.setItemText(4, QCoreApplication.translate("userMainMenu", u"account's owner", None))
        self.action_cmb.setItemText(5, QCoreApplication.translate("userMainMenu", u"block account", None))
        self.action_cmb.setItemText(6, QCoreApplication.translate("userMainMenu", u"transfer", None))
        self.action_cmb.setItemText(7, QCoreApplication.translate("userMainMenu", u"get new loan", None))
        self.action_cmb.setItemText(8, QCoreApplication.translate("userMainMenu", u"current loans", None))
        self.action_cmb.setItemText(9, QCoreApplication.translate("userMainMenu", u"instalments", None))

        self.action_pbn.setText(QCoreApplication.translate("userMainMenu", u"OK", None))
        self.new_password_lbl.setText(QCoreApplication.translate("userMainMenu", u"new password:", None))
        self.action_done_pbn.setText(QCoreApplication.translate("userMainMenu", u"DONE", None))
        self.number_lbl.setText(QCoreApplication.translate("userMainMenu", u"number:", None))
        self.const_lbl.setText(QCoreApplication.translate("userMainMenu", u"current balance:", None))
        self.balance_lbl.setText(QCoreApplication.translate("userMainMenu", u"0", None))
    # retranslateUi

