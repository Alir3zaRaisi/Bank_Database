# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainPage.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


from PySide2 import QtWidgets
from PySide2.QtCore import *
from PySide2.QtWidgets import *

#import user
from ui_chooseAccount import Ui_chooseAccount
from ui_wrongPass import Ui_wrongPass
from ui_signUp import Ui_signUp


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
        self.user_led = QLineEdit(self.gridLayoutWidget)
        self.user_led.setObjectName(u"user_led")

        self.gridLayout.addWidget(self.user_led, 3, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sign_up_pbn = QPushButton(self.gridLayoutWidget)
        self.sign_up_pbn.setObjectName(u"sign_up_pbn")

        self.horizontalLayout.addWidget(self.sign_up_pbn)


        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 1)

        self.password_led = QLineEdit(self.gridLayoutWidget)
        self.password_led.setObjectName(u"password_led")

        self.gridLayout.addWidget(self.password_led, 5, 1, 1, 1)

        self.enter_pbn = QPushButton(self.gridLayoutWidget)
        self.enter_pbn.setObjectName(u"enter_pbn")

        self.gridLayout.addWidget(self.enter_pbn, 6, 1, 1, 1)

        self.user_lbl = QLabel(self.gridLayoutWidget)
        self.user_lbl.setObjectName(u"user_lbl")

        self.gridLayout.addWidget(self.user_lbl, 3, 0, 1, 1)

        self.password_lbl = QLabel(self.gridLayoutWidget)
        self.password_lbl.setObjectName(u"password_lbl")

        self.gridLayout.addWidget(self.password_lbl, 5, 0, 1, 1)

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
        self.sign_up_pbn.clicked.connect(self.createNewAccount)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.sign_up_pbn.setText(QCoreApplication.translate("MainWindow", u"sign up", None))
        self.enter_pbn.setText(QCoreApplication.translate("MainWindow", u"sign in", None))
        self.user_lbl.setText(QCoreApplication.translate("MainWindow", u"username", None))
        self.password_lbl.setText(QCoreApplication.translate("MainWindow", u"password", None))
        self.welcome_lbl.setText(QCoreApplication.translate("MainWindow", u"welcome to miniBank!", None))
    # retranslateUi


    #slots
    @Slot()
    def createNewAccount(self):
        self.ex = Ui_signUp()
        self.w = QtWidgets.QWidget()
        self.ex.setupUi(self.w)
        self.w.show()

        # refresh ui
        self.ex.retranslateUi
        self.w.show()

    @Slot()
    def checkUserNamePassword(self):
     username_ui = self.user_led.text()
     password_ui = self.password_led.text()

     # alireza
     # get user data and set it for user

#     result = user.check_credentials(username_ui, password_ui)
#     full_name, user_id = result

     #for front-end testing
     full_name = None
     if username_ui == 'root' and password_ui == 'root':
         full_name = 'new root name'
     #end front-end testing

     #alireza
     #must retrieve owner's name and set full_name variable as owner's name

     print(full_name)
     if full_name is not None:
         # if user and password are right
         self.ex = Ui_chooseAccount()

         self.ex.owner_name = full_name

         self.w = QtWidgets.QWidget()
         self.ex.setupUi(self.w)
         # update users accounts
#         accounts = user.get_account_credentials(user_id)
         # account_number, balance, status
         # must be filled with users accounts
         for i in range(5):
             self.ex.choose_account_cmb.addItem(str(i))
             # print(account)
     else:
         # if user or password is wrong
         self.ex = Ui_wrongPass()
         self.w = QtWidgets.QWidget()
         self.ex.setupUi(self.w)
         self.w.show()

         # refresh ui
     self.ex.retranslateUi

     self.w.show()
