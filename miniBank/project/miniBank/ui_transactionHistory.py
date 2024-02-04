# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'transactionHistory.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_transactionHistory(object):
    def setupUi(self, transactionHistory):
        if not transactionHistory.objectName():
            transactionHistory.setObjectName(u"transactionHistory")
        transactionHistory.resize(961, 605)
        self.transation_history_tbl = QTableWidget(transactionHistory)
        self.transation_history_tbl.setObjectName(u"transation_history_tbl")
        self.transation_history_tbl.setGeometry(QRect(20, 40, 921, 541))
        self.source_account_lbl = QLabel(transactionHistory)
        self.source_account_lbl.setObjectName(u"source_account_lbl")
        self.source_account_lbl.setGeometry(QRect(30, 60, 121, 16))
        self.dest_account_lbl = QLabel(transactionHistory)
        self.dest_account_lbl.setObjectName(u"dest_account_lbl")
        self.dest_account_lbl.setGeometry(QRect(240, 60, 161, 16))
        self.transaction_amount_lbl = QLabel(transactionHistory)
        self.transaction_amount_lbl.setObjectName(u"transaction_amount_lbl")
        self.transaction_amount_lbl.setGeometry(QRect(450, 60, 191, 16))
        self.balance_lbl = QLabel(transactionHistory)
        self.balance_lbl.setObjectName(u"balance_lbl")
        self.balance_lbl.setGeometry(QRect(624, 60, 111, 20))
        self.date_lbl = QLabel(transactionHistory)
        self.date_lbl.setObjectName(u"date_lbl")
        self.date_lbl.setGeometry(QRect(714, 60, 181, 20))

        self.retranslateUi(transactionHistory)

        QMetaObject.connectSlotsByName(transactionHistory)
    # setupUi

    def retranslateUi(self, transactionHistory):
        transactionHistory.setWindowTitle(QCoreApplication.translate("transactionHistory", u"Form", None))
        self.source_account_lbl.setText(QCoreApplication.translate("transactionHistory", u"src. account", None))
        self.dest_account_lbl.setText(QCoreApplication.translate("transactionHistory", u"dest. account", None))
        self.transaction_amount_lbl.setText(QCoreApplication.translate("transactionHistory", u"transaction amount", None))
        self.balance_lbl.setText(QCoreApplication.translate("transactionHistory", u"balance", None))
        self.date_lbl.setText(QCoreApplication.translate("transactionHistory", u"date", None))
    # retranslateUi

