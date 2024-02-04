# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'accountInfo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_accountInfo(object):
    def setupUi(self, accountInfo):
        if not accountInfo.objectName():
            accountInfo.setObjectName(u"accountInfo")
        accountInfo.resize(400, 300)
        self.ok_pbn = QPushButton(accountInfo)
        self.ok_pbn.setObjectName(u"ok_pbn")
        self.ok_pbn.setGeometry(QRect(240, 240, 93, 28))
        self.verticalLayoutWidget = QWidget(accountInfo)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(60, 80, 160, 151))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.owner_lbl = QLabel(self.verticalLayoutWidget)
        self.owner_lbl.setObjectName(u"owner_lbl")

        self.verticalLayout.addWidget(self.owner_lbl)

        self.balance_lbl = QLabel(self.verticalLayoutWidget)
        self.balance_lbl.setObjectName(u"balance_lbl")

        self.verticalLayout.addWidget(self.balance_lbl)

        self.is_blocked_lbl = QLabel(self.verticalLayoutWidget)
        self.is_blocked_lbl.setObjectName(u"is_blocked_lbl")

        self.verticalLayout.addWidget(self.is_blocked_lbl)


        self.retranslateUi(accountInfo)
        self.ok_pbn.clicked.connect(accountInfo.close)

        QMetaObject.connectSlotsByName(accountInfo)
    # setupUi

    def retranslateUi(self, accountInfo):
        accountInfo.setWindowTitle(QCoreApplication.translate("accountInfo", u"Form", None))
        self.ok_pbn.setText(QCoreApplication.translate("accountInfo", u"OK", None))
        self.owner_lbl.setText(QCoreApplication.translate("accountInfo", u"owner: ", None))
        self.balance_lbl.setText(QCoreApplication.translate("accountInfo", u"balance: ", None))
        self.is_blocked_lbl.setText(QCoreApplication.translate("accountInfo", u"is blocked: ", None))
    # retranslateUi

