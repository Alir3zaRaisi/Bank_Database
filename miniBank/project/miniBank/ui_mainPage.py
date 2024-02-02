# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainPage.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


from PySide2 import QtWidgets
from ui_wrongPass import Ui_wrongPass

from ui_chooseAccount import Ui_chooseAccount


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(616, 543)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(240, 170, 211, 221))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 1)

        self.username_lbl = QLabel(self.gridLayoutWidget)
        self.username_lbl.setObjectName(u"username_lbl")

        self.gridLayout.addWidget(self.username_lbl, 3, 0, 1, 1)

        self.password_led = QLineEdit(self.gridLayoutWidget)
        self.password_led.setObjectName(u"password_led")

        self.gridLayout.addWidget(self.password_led, 5, 1, 1, 1)

        self.username_led = QLineEdit(self.gridLayoutWidget)
        self.username_led.setObjectName(u"username_led")

        self.gridLayout.addWidget(self.username_led, 3, 1, 1, 1)

        self.password_lbl = QLabel(self.gridLayoutWidget)
        self.password_lbl.setObjectName(u"password_lbl")

        self.gridLayout.addWidget(self.password_lbl, 5, 0, 1, 1)

        self.enter_pbn = QPushButton(self.gridLayoutWidget)
        self.enter_pbn.setObjectName(u"enter_pbn")

        self.gridLayout.addWidget(self.enter_pbn, 6, 1, 1, 1)

        self.welcome_lbl = QLabel(self.centralwidget)
        self.welcome_lbl.setObjectName(u"welcome_lbl")
        self.welcome_lbl.setGeometry(QRect(70, 70, 151, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 616, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #connect
        #signal.connect(slot)
        self.enter_pbn.clicked.connect(self.checkUserNamePassword)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.username_lbl.setText(QCoreApplication.translate("MainWindow", u"username", None))
        self.password_lbl.setText(QCoreApplication.translate("MainWindow", u"password", None))
        self.enter_pbn.setText(QCoreApplication.translate("MainWindow", u"enter", None))
        self.welcome_lbl.setText(QCoreApplication.translate("MainWindow", u"welcome to miniBank!", None))
    # retranslateUi

    #slots
    @Slot()
    def checkUserNamePassword(self):
        username_ui = self.username_led.text()
        password_ui = self.password_led.text()

        #alireza
            #get user data and set it for user

        #if user or password is wrong
        self.ex = Ui_wrongPass()
        self.w = QtWidgets.QWidget()
        self.ex.setupUi(self.w)
        self.w.show()

        #if user and password are right
        self.ex = Ui_chooseAccount()
        self.w = QtWidgets.QWidget()
        self.ex.setupUi(self.w)
            #update name
        self.ex.welcome_lbl.setText(self.ex.welcome_lbl.text() + " ali!")
            #update users accounts
            #must be filled with users accounts
        self.ex.choose_account_cmb.addItem("123")
        self.ex.choose_account_cmb.addItem("456")

            #refresh ui
        self.ex.retranslateUi

        self.w.show()




