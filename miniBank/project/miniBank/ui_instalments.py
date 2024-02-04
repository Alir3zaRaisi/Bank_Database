# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'instalments.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_instalments(object):
    def setupUi(self, instalments):
        if not instalments.objectName():
            instalments.setObjectName(u"instalments")
        instalments.resize(400, 300)
        self.verticalLayoutWidget = QWidget(instalments)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(50, 19, 301, 191))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.num_of_paids_lbl = QLabel(self.verticalLayoutWidget)
        self.num_of_paids_lbl.setObjectName(u"num_of_paids_lbl")

        self.verticalLayout.addWidget(self.num_of_paids_lbl)

        self.num_of_unpaids_lbl = QLabel(self.verticalLayoutWidget)
        self.num_of_unpaids_lbl.setObjectName(u"num_of_unpaids_lbl")

        self.verticalLayout.addWidget(self.num_of_unpaids_lbl)

        self.sum_of_remainings_lbl = QLabel(self.verticalLayoutWidget)
        self.sum_of_remainings_lbl.setObjectName(u"sum_of_remainings_lbl")

        self.verticalLayout.addWidget(self.sum_of_remainings_lbl)

        self.sum_of_paids_lbl = QLabel(self.verticalLayoutWidget)
        self.sum_of_paids_lbl.setObjectName(u"sum_of_paids_lbl")

        self.verticalLayout.addWidget(self.sum_of_paids_lbl)

        self.ok_pbn = QPushButton(instalments)
        self.ok_pbn.setObjectName(u"ok_pbn")
        self.ok_pbn.setGeometry(QRect(260, 230, 93, 28))

        self.retranslateUi(instalments)
        self.ok_pbn.clicked.connect(instalments.close)

        QMetaObject.connectSlotsByName(instalments)
    # setupUi

    def retranslateUi(self, instalments):
        instalments.setWindowTitle(QCoreApplication.translate("instalments", u"Form", None))
        self.num_of_paids_lbl.setText(QCoreApplication.translate("instalments", u"#paids: ", None))
        self.num_of_unpaids_lbl.setText(QCoreApplication.translate("instalments", u"#unpaids: ", None))
        self.sum_of_remainings_lbl.setText(QCoreApplication.translate("instalments", u"sum(remainings): ", None))
        self.sum_of_paids_lbl.setText(QCoreApplication.translate("instalments", u"sum(paids): ", None))
        self.ok_pbn.setText(QCoreApplication.translate("instalments", u"OK", None))
    # retranslateUi

