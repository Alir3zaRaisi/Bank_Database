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
from ui_infoBox import Ui_infoBox


class Ui_userMainMenu(object):
    def hideAll(self):
        #hide on start
        self.new_password_lbl.hide()
        self.new_password_led.hide()
        self.number_lbl.hide()
        self.number_led.hide()
        self.start_date_lbl.hide()
        self.start_date_led.hide()
        self.end_date_lbl.hide()
        self.end_date_led.hide()
        self.account_number_lbl.hide()
        self.account_number_led.hide()
        self.amount_lbl.hide()
        self.amount_led.hide()
        self.loan_lbl.hide()
        self.loan_cmb.hide()
        self.action_done_pbn.hide()

    def setupUi(self, userMainMenu):
        if not userMainMenu.objectName():
            userMainMenu.setObjectName(u"userMainMenu")
        userMainMenu.resize(733, 480)
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
        self.action_cmb.setGeometry(QRect(20, 140, 161, 22))
        self.action_pbn = QPushButton(userMainMenu)
        self.action_pbn.setObjectName(u"action_pbn")
        self.action_pbn.setGeometry(QRect(40, 220, 93, 28))
        self.formLayoutWidget = QWidget(userMainMenu)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(222, 100, 451, 261))
        self.chosenAction_lyt = QFormLayout(self.formLayoutWidget)
        self.chosenAction_lyt.setObjectName(u"chosenAction_lyt")
        self.chosenAction_lyt.setContentsMargins(0, 0, 0, 0)
        self.new_password_lbl = QLabel(self.formLayoutWidget)
        self.new_password_lbl.setObjectName(u"new_password_lbl")
        self.new_password_lbl.setEnabled(True)

        self.chosenAction_lyt.setWidget(0, QFormLayout.LabelRole, self.new_password_lbl)

        self.new_password_led = QLineEdit(self.formLayoutWidget)
        self.new_password_led.setObjectName(u"new_password_led")
        self.new_password_led.setEnabled(True)

        self.chosenAction_lyt.setWidget(0, QFormLayout.FieldRole, self.new_password_led)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.chosenAction_lyt.setItem(7, QFormLayout.LabelRole, self.horizontalSpacer)

        self.action_done_pbn = QPushButton(self.formLayoutWidget)
        self.action_done_pbn.setObjectName(u"action_done_pbn")
        self.action_done_pbn.setEnabled(True)

        self.chosenAction_lyt.setWidget(7, QFormLayout.FieldRole, self.action_done_pbn)

        self.number_lbl = QLabel(self.formLayoutWidget)
        self.number_lbl.setObjectName(u"number_lbl")
        self.number_lbl.setEnabled(True)

        self.chosenAction_lyt.setWidget(1, QFormLayout.LabelRole, self.number_lbl)

        self.number_led = QLineEdit(self.formLayoutWidget)
        self.number_led.setObjectName(u"number_led")
        self.number_led.setEnabled(True)

        self.chosenAction_lyt.setWidget(1, QFormLayout.FieldRole, self.number_led)

        self.start_date_lbl = QLabel(self.formLayoutWidget)
        self.start_date_lbl.setObjectName(u"start_date_lbl")
        self.start_date_lbl.setEnabled(True)

        self.chosenAction_lyt.setWidget(2, QFormLayout.LabelRole, self.start_date_lbl)

        self.end_date_lbl = QLabel(self.formLayoutWidget)
        self.end_date_lbl.setObjectName(u"end_date_lbl")
        self.end_date_lbl.setEnabled(True)

        self.chosenAction_lyt.setWidget(3, QFormLayout.LabelRole, self.end_date_lbl)

        self.start_date_led = QLineEdit(self.formLayoutWidget)
        self.start_date_led.setObjectName(u"start_date_led")
        self.start_date_led.setEnabled(True)

        self.chosenAction_lyt.setWidget(2, QFormLayout.FieldRole, self.start_date_led)

        self.end_date_led = QLineEdit(self.formLayoutWidget)
        self.end_date_led.setObjectName(u"end_date_led")
        self.end_date_led.setEnabled(True)

        self.chosenAction_lyt.setWidget(3, QFormLayout.FieldRole, self.end_date_led)

        self.account_number_lbl = QLabel(self.formLayoutWidget)
        self.account_number_lbl.setObjectName(u"account_number_lbl")
        self.account_number_lbl.setEnabled(True)

        self.chosenAction_lyt.setWidget(4, QFormLayout.LabelRole, self.account_number_lbl)

        self.account_number_led = QLineEdit(self.formLayoutWidget)
        self.account_number_led.setObjectName(u"account_number_led")
        self.account_number_led.setEnabled(True)

        self.chosenAction_lyt.setWidget(4, QFormLayout.FieldRole, self.account_number_led)

        self.amount_lbl = QLabel(self.formLayoutWidget)
        self.amount_lbl.setObjectName(u"amount_lbl")
        self.amount_lbl.setEnabled(True)

        self.chosenAction_lyt.setWidget(5, QFormLayout.LabelRole, self.amount_lbl)

        self.amount_led = QLineEdit(self.formLayoutWidget)
        self.amount_led.setObjectName(u"amount_led")
        self.amount_led.setEnabled(True)

        self.chosenAction_lyt.setWidget(5, QFormLayout.FieldRole, self.amount_led)

        self.loan_lbl = QLabel(self.formLayoutWidget)
        self.loan_lbl.setObjectName(u"loan_lbl")
        self.loan_lbl.setEnabled(True)

        self.chosenAction_lyt.setWidget(6, QFormLayout.LabelRole, self.loan_lbl)

        self.loan_cmb = QComboBox(self.formLayoutWidget)
        self.loan_cmb.setObjectName(u"loan_cmb")
        self.loan_cmb.setEnabled(True)

        self.chosenAction_lyt.setWidget(6, QFormLayout.FieldRole, self.loan_cmb)

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


        self.hideAll()

        #connect
        self.action_pbn.clicked.connect(self.actionChosen)
        self.action_done_pbn.clicked.connect(self.doAction)

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
        self.start_date_lbl.setText(QCoreApplication.translate("userMainMenu", u"start date: ", None))
        self.end_date_lbl.setText(QCoreApplication.translate("userMainMenu", u"end date: ", None))
        self.account_number_lbl.setText(QCoreApplication.translate("userMainMenu", u"account number: ", None))
        self.amount_lbl.setText(QCoreApplication.translate("userMainMenu", u"amount: ", None))
        self.loan_lbl.setText(QCoreApplication.translate("userMainMenu", u"select loan: ", None))
        self.const_lbl.setText(QCoreApplication.translate("userMainMenu", u"current balance:", None))
        self.balance_lbl.setText(QCoreApplication.translate("userMainMenu", u"0", None))
    # retranslateUi



    @Slot()
    def doAction(self):
        currentAction = self.action_cmb.currentText()
        if currentAction == "change password":
            new_chosen_password = self.new_password_led.text()
            #alireza
            #store it in database

        if currentAction == "recent transactions":
            pass

        if currentAction == "transactions - time based":
            pass

        if currentAction == "account's info" or currentAction == "account's owner":
            pass

        if currentAction == "block account":
            pass

        if currentAction == "transfer":
            pass

        if currentAction == "get new loan":
            pass

        if currentAction == "current loans":
            pass

        if currentAction == "instalments":
            pass


    def actionChosen(self):
        currentAction = self.action_cmb.currentText()

        if currentAction == "change password":
            self.hideAll()
            self.action_done_pbn.show()
            self.new_password_lbl.show()
            self.new_password_led.show()
            new_chosen_password = self.new_password_led.text()
            #alireza
            #store it in database

            self.ex = Ui_infoBox()
            self.ex.label.setText("password changed.")
            self.w = QtWidgets.QWidget()
            self.ex.setupUi(self.w)
            self.w.show()

            # refresh ui
            self.ex.retranslateUi
            self.w.show()


        if currentAction == "recent transactions":
            self.hideAll()
            self.action_done_pbn.show()
            self.number_lbl.show()
            self.number_led.show()


        if currentAction == "transactions - time based":
            self.hideAll()
            self.action_done_pbn.show()
            self.start_date_lbl.show()
            self.start_date_led.show()
            self.end_date_lbl.show()
            self.end_date_led.show()

        if currentAction == "account's info" or currentAction == "account's owner":
            self.hideAll()
            self.action_done_pbn.show()
            self.account_number_lbl.show()
            self.account_number_led.show()

        if currentAction == "block account":
            self.hideAll()
            self.action_done_pbn.show()
            pass

        if currentAction == "transfer":
            hideAll()
            self.action_done_pbn.show()
            self.amount_lbl.show()
            self.amount_led.show()

        if currentAction == "get new loan":
            self.hideAll()
            self.action_done_pbn.show()
            self.loan_lbl.show()
            self.loan_cmb.show()

        if currentAction == "current loans":
            self.hideAll()
            self.action_done_pbn.show()
            pass

        if currentAction == "instalments":
            self.hideAll()
            self.action_done_pbn.show()
            pass
