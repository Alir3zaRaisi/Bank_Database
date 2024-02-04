# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loans.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_loans(object):
    def setupUi(self, loans):
        if not loans.objectName():
            loans.setObjectName(u"loans")
        loans.resize(961, 605)
        self.transation_history_tbl = QTableWidget(loans)
        self.transation_history_tbl.setObjectName(u"transation_history_tbl")
        self.transation_history_tbl.setGeometry(QRect(20, 40, 921, 541))
        self.account_number_lbl = QLabel(loans)
        self.account_number_lbl.setObjectName(u"account_number_lbl")
        self.account_number_lbl.setGeometry(QRect(50, 60, 121, 16))
        self.loan_number_lbl = QLabel(loans)
        self.loan_number_lbl.setObjectName(u"loan_number_lbl")
        self.loan_number_lbl.setGeometry(QRect(260, 60, 161, 16))
        self.loan_amount_lbl = QLabel(loans)
        self.loan_amount_lbl.setObjectName(u"loan_amount_lbl")
        self.loan_amount_lbl.setGeometry(QRect(470, 60, 191, 16))
        self.balance_lbl = QLabel(loans)
        self.balance_lbl.setObjectName(u"balance_lbl")
        self.balance_lbl.setGeometry(QRect(690, 60, 111, 20))

        self.retranslateUi(loans)

        QMetaObject.connectSlotsByName(loans)
    # setupUi

    def retranslateUi(self, loans):
        loans.setWindowTitle(QCoreApplication.translate("loans", u"Form", None))
        self.account_number_lbl.setText(QCoreApplication.translate("loans", u"account number", None))
        self.loan_number_lbl.setText(QCoreApplication.translate("loans", u"loan number", None))
        self.loan_amount_lbl.setText(QCoreApplication.translate("loans", u"loan amount", None))
        self.balance_lbl.setText(QCoreApplication.translate("loans", u"loan status", None))
    # retranslateUi

