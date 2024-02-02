import sys
from PySide2.QtWidgets import QApplication
from PySide2 import QtWidgets
from ui_mainPage import Ui_MainWindow




if __name__ == "__main__":
    app = QApplication([])
    ex = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())
