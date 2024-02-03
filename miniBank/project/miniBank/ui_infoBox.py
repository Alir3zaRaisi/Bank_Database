# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'infoBox.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_infoBox(object):
    def setupUi(self, infoBox):
        if not infoBox.objectName():
            infoBox.setObjectName(u"infoBox")
        infoBox.resize(400, 300)
        self.label = QLabel(infoBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 65, 251, 61))
        self.pushButton = QPushButton(infoBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(250, 230, 121, 31))

        self.retranslateUi(infoBox)
        self.pushButton.clicked.connect(infoBox.close)

        QMetaObject.connectSlotsByName(infoBox)
    # setupUi

    def retranslateUi(self, infoBox):
        infoBox.setWindowTitle(QCoreApplication.translate("infoBox", u"Form", None))
        self.label.setText(QCoreApplication.translate("infoBox", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("infoBox", u"OK", None))
    # retranslateUi

