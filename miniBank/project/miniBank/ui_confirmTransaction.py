# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirmTransaction.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui_infoBox import Ui_infoBox
from PySide2 import QtWidgets


class Ui_confirmTranaction(object):
    owner_name = "default name"
    amount = 1
    def setupUi(self, confirmTranaction):
        if not confirmTranaction.objectName():
            confirmTranaction.setObjectName(u"confirmTranaction")
        confirmTranaction.resize(400, 300)
        self.from_lbl = QLabel(confirmTranaction)
        self.from_lbl.setObjectName(u"from_lbl")
        self.from_lbl.setGeometry(QRect(20, 40, 55, 16))
        self.to_lbl = QLabel(confirmTranaction)
        self.to_lbl.setObjectName(u"to_lbl")
        self.to_lbl.setGeometry(QRect(20, 100, 55, 16))
        self.amount_lbl = QLabel(confirmTranaction)
        self.amount_lbl.setObjectName(u"amount_lbl")
        self.amount_lbl.setGeometry(QRect(20, 140, 55, 16))
        self.label_4 = QLabel(confirmTranaction)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 180, 361, 71))
        self.confirm_pbn = QPushButton(confirmTranaction)
        self.confirm_pbn.setObjectName(u"confirm_pbn")
        self.confirm_pbn.setGeometry(QRect(140, 250, 93, 28))

        #connect
        self.confirm_pbn.clicked.connect(self.doTransaction)

        self.retranslateUi(confirmTranaction)

        QMetaObject.connectSlotsByName(confirmTranaction)
    # setupUi

    def retranslateUi(self, confirmTranaction):
        confirmTranaction.setWindowTitle(QCoreApplication.translate("confirmTranaction", u"Form", None))
        self.from_lbl.setText(QCoreApplication.translate("confirmTranaction", u"from: ", None))
        self.to_lbl.setText(QCoreApplication.translate("confirmTranaction", u"to: ", None))
        self.amount_lbl.setText(QCoreApplication.translate("confirmTranaction", u"amount: ", None))
        self.label_4.setText(QCoreApplication.translate("confirmTranaction", u"are you sure you want to continue with the transction above?", None))
        self.confirm_pbn.setText(QCoreApplication.translate("confirmTranaction", u"confirm", None))
        self.from_lbl.setText("from: " + self.owner_name)
        self.amount_lbl.setText("amount: " + self.amount)
    # retranslateUi

    @Slot()
    def doTransaction(self):
        self.ex = Ui_infoBox()
        self.w = QtWidgets.QWidget()
        self.ex.setupUi(self.w)

        #alireza
        # one of the following must be shown
        #if can do the transaction
        self.ex.label.setText("transaction complete")
        #if can't do the transaction
        self.ex.label.setText("transaction failed")

        self.ex.retranslateUi
        self.w.show()
