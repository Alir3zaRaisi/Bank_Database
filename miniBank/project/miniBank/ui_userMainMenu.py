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

from ui_transactionHistory import Ui_transactionHistory
from ui_loans import Ui_loans
from ui_instalments import Ui_instalments

from ui_infoBox import Ui_infoBox
from ui_accountInfo import Ui_accountInfo
from PySide2 import QtWidgets
from ui_confirmTransaction import Ui_confirmTranaction



class Ui_userMainMenu(object):
    account_index = 0
    owner_name = "default_name"
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
        self.loan_point_lbl.hide()
        self.loan_amount_lbl.hide()
        self.loan_amount_led.hide()
        self.loan_number_lbl.hide()
        self.loan_number_led.hide()
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
        self.action_cmb.setObjectName(u"action_cmb")
        self.action_cmb.setGeometry(QRect(20, 140, 161, 22))
        self.action_pbn = QPushButton(userMainMenu)
        self.action_pbn.setObjectName(u"action_pbn")
        self.action_pbn.setGeometry(QRect(40, 220, 93, 28))
        self.formLayoutWidget = QWidget(userMainMenu)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(222, 100, 451, 280))
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

        self.chosenAction_lyt.setItem(8, QFormLayout.LabelRole, self.horizontalSpacer)

        self.action_done_pbn = QPushButton(self.formLayoutWidget)
        self.action_done_pbn.setObjectName(u"action_done_pbn")
        self.action_done_pbn.setEnabled(True)

        self.chosenAction_lyt.setWidget(8, QFormLayout.FieldRole, self.action_done_pbn)

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

        self.loan_point_lbl = QLabel(self.formLayoutWidget)
        self.loan_point_lbl.setObjectName(u"loan_point_lbl")
        self.loan_point_lbl.setEnabled(True)

        self.chosenAction_lyt.setWidget(6, QFormLayout.LabelRole, self.loan_point_lbl)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.loan_amount_lbl = QLabel(self.formLayoutWidget)
        self.loan_amount_lbl.setObjectName(u"loan_amount_lbl")

        self.horizontalLayout.addWidget(self.loan_amount_lbl)

        self.loan_amount_led = QLineEdit(self.formLayoutWidget)
        self.loan_amount_led.setObjectName(u"loan_amount_led")

        self.horizontalLayout.addWidget(self.loan_amount_led)


        self.chosenAction_lyt.setLayout(6, QFormLayout.FieldRole, self.horizontalLayout)

        self.loan_number_lbl = QLabel(self.formLayoutWidget)
        self.loan_number_lbl.setObjectName(u"loan_number_lbl")

        self.chosenAction_lyt.setWidget(7, QFormLayout.LabelRole, self.loan_number_lbl)

        self.loan_number_led = QLineEdit(self.formLayoutWidget)
        self.loan_number_led.setObjectName(u"loan_number_led")

        self.chosenAction_lyt.setWidget(7, QFormLayout.FieldRole, self.loan_number_led)

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
        self.action_cmb.setItemText(4, QCoreApplication.translate("userMainMenu", u"block account", None))
        self.action_cmb.setItemText(5, QCoreApplication.translate("userMainMenu", u"transfer", None))
        self.action_cmb.setItemText(6, QCoreApplication.translate("userMainMenu", u"get new loan", None))
        self.action_cmb.setItemText(7, QCoreApplication.translate("userMainMenu", u"current loans", None))
        self.action_cmb.setItemText(8, QCoreApplication.translate("userMainMenu", u"instalments", None))

        self.action_pbn.setText(QCoreApplication.translate("userMainMenu", u"OK", None))
        self.new_password_lbl.setText(QCoreApplication.translate("userMainMenu", u"new password:", None))
        self.action_done_pbn.setText(QCoreApplication.translate("userMainMenu", u"DONE", None))
        self.number_lbl.setText(QCoreApplication.translate("userMainMenu", u"number:", None))
        self.start_date_lbl.setText(QCoreApplication.translate("userMainMenu", u"start date: ", None))
        self.end_date_lbl.setText(QCoreApplication.translate("userMainMenu", u"end date: ", None))
        self.account_number_lbl.setText(QCoreApplication.translate("userMainMenu", u"account number: ", None))
        self.amount_lbl.setText(QCoreApplication.translate("userMainMenu", u"amount: ", None))
        self.loan_point_lbl.setText(QCoreApplication.translate("userMainMenu", u"loan point: ", None))
        self.loan_amount_lbl.setText(QCoreApplication.translate("userMainMenu", u"loan amount: ", None))
        self.loan_number_lbl.setText(QCoreApplication.translate("userMainMenu", u"loan number: ", None))
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
            self.ex = Ui_infoBox()
            self.w = QtWidgets.QWidget()
            self.ex.setupUi(self.w)
            self.ex.label.setText("password changed.")


        if currentAction == "recent transactions":
            number_of_transactions = self.number_led.text()
            #alireza
            #retrieve data from database
            self.ex = Ui_transactionHistory()
            self.w = QtWidgets.QWidget()
            self.ex.setupUi(self.w)


        if currentAction == "transactions - time based":
            start_date = self.start_date_led.text()
            end_date = self.end_date_led.text()
            #alireza
            #retrieve data from database
            self.ex = Ui_transactionHistory()
            self.w = QtWidgets.QWidget()
            self.ex.setupUi(self.w)
            self.ex.label.setText("recent transactions: (based on time)")


        if currentAction == "account's info":
            account_number = self.account_number_led.text()
            #alireza
            #retrieve data from database
            self.ex = Ui_accountInfo()
            self.w = QtWidgets.QWidget()
            self.ex.setupUi(self.w)
            #labels must be updated based on stored data

        if currentAction == "block account":
            #alireza
            #remove current account from database
            self.ex = Ui_infoBox()
            self.w = QtWidgets.QWidget()
            self.ex.setupUi(self.w)
            self.ex.label.setText("current account deleted from database")

        if currentAction == "transfer":
            destination_address = self.account_number_led.text()
            amount = self.amount_led.text()
            #alireza
            #store transaction
            self.ex = Ui_confirmTranaction()
            self.ex.amount = amount
            self.ex.owner_name = self.owner_name
            self.w = QtWidgets.QWidget()
            self.ex.setupUi(self.w)
            self.ex.retranslateUi

            #alireza
            #set from, to, amount labels with proper amounts
    #            self.ex.from_lbl.setText(self.ex.from_lbl.text() +  )
    #            self.ex.to_lbl.setText(self.ex.to_lbl.text() +  )

    #            self.ex.retranslateUi


        if currentAction == "get new loan":
            chosen_loan = self.loan_amount_led.text()
            #alireza
            #check loan
            self.ex = Ui_infoBox()
            self.w = QtWidgets.QWidget()


            self.ex.setupUi(self.w)

            #alireza
            # one of the following must be shown
            #if can recieve loan
            self.ex.label.setText("loan recieved")
            #if can't recieve loan
            self.ex.label.setText("loan failed")

        if currentAction == "current loans":
            #alireza
            #get loan from database
            self.ex = Ui_loans()
            self.w = QtWidgets.QWidget()
            self.ex.setupUi(self.w)


        if currentAction == "instalments":
            #alireza
            #get loan's info from database
            self.ex = Ui_instalments()
            self.w = QtWidgets.QWidget()
            self.ex.setupUi(self.w)

            #alireza

        self.w.show()

        # refresh ui
        self.ex.retranslateUi
        self.w.show()


    def actionChosen(self):
        currentAction = self.action_cmb.currentText()

        if currentAction == "change password":
            self.hideAll()
            self.action_done_pbn.show()
            self.new_password_lbl.show()
            self.new_password_led.show()

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

        if currentAction == "account's info":
            self.hideAll()
            self.action_done_pbn.show()
            self.account_number_lbl.show()
            self.account_number_led.show()

        if currentAction == "block account":
            self.hideAll()
            self.action_done_pbn.show()
            pass

        if currentAction == "transfer":
            self.hideAll()
            self.action_done_pbn.show()
            self.amount_lbl.show()
            self.amount_led.show()
            self.account_number_lbl.show()
            self.account_number_led.show()

        if currentAction == "get new loan":
            self.hideAll()
            self.action_done_pbn.show()
            self.loan_point_lbl.show()
            self.loan_amount_lbl.show()
            self.loan_amount_led.show()
            #alireza
            #loan point must be calulated
            #must update loan_point_lbl by the value calculated in last step
            #must store new loan if user presses done button

        if currentAction == "current loans":
            self.hideAll()
            self.action_done_pbn.show()

        if currentAction == "instalments":
            self.hideAll()
            self.loan_number_lbl.show()
            self.loan_number_led.show()
            self.action_done_pbn.show()



