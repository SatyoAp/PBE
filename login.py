from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import sys


class Ui_MainWindow(object):

    def login(self):
        username = self.txusername.text()  # mendefinisikan line edit username
        password = self.txtpass.text()  # mendefinisikan line edit password

        if (username and password != ""):
            koneksi = sqlite3.connect("dbjimpitan.db")
            cur = koneksi.cursor()
            cur.execute(
                "SELECT * FROM akun WHERE username=? AND password=?", (username, password))
            baris = cur.fetchone()
            if (baris == None):           # Kondisi jika data tidak ditemukan di database
                self.warningBox(
                    "Eror", "Username atau Password salah")
            else:
                self.messageBox("Berhasil", "Login Berhasil")
                koneksi.close()
        else:
            self.warningBox(
                "Eror", "Username atau Password tidak boleh kosong")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(509, 381)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txusername = QtWidgets.QLineEdit(self.centralwidget)
        self.txusername.setGeometry(QtCore.QRect(150, 70, 113, 20))
        self.txusername.setObjectName("txusername")
        self.txtpass = QtWidgets.QLineEdit(self.centralwidget)
        self.txtpass.setGeometry(QtCore.QRect(150, 120, 113, 20))
        self.txtpass.setObjectName("txtpass")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 80, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 47, 13))
        self.label_2.setObjectName("label_2")
        self.btlogin = QtWidgets.QPushButton(self.centralwidget)
        self.btlogin.setGeometry(QtCore.QRect(170, 180, 75, 23))
        self.btlogin.setObjectName("btlogin")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 509, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.btlogin.setText(_translate("MainWindow", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
