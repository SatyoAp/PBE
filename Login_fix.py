from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import sqlite3
from Main_Menu_fix import main_utama


class login(object):
    def tampilmain(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = main_utama()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        MainWindow.hide()

    def messageBox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setIcon(QtWidgets.QMessageBox.Information)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def warningBox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setIcon(QtWidgets.QMessageBox.Warning)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def login(self):
        username = self.txtUsername.text()  # mendefinisikan line edit username
        password = self.txtPassword.text()  # mendefinisikan line edit password

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
                self.tampilmain()
                koneksi.close()
        else:
            self.warningBox(
                "Eror", "Username atau Password tidak boleh kosong")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(507, 514)
        MainWindow.setStyleSheet("QPushButton#btnLogin{\n"
                                 "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(68, 23, 23, 255));\n"
                                 "    color: rgb(255, 255, 255);\n"
                                 "    border-radius:15px;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton#btnLogin:hover{\n"
                                 "    background-color: rgb(170, 0, 0);\n"
                                 "}\n"
                                 "QPushButton#btnLogin:pressed{\n"
                                 "    padding-left:2px;\n"
                                 "    padding-top:2px;\n"
                                 "    background-color: rgb(179, 59, 59);;\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 40, 391, 411))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "border-radius: 50px;\n"
                                   "border-top-right-radius: 50px;\n"
                                   "\n"
                                   "")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 90, 101, 51))
        self.label.setObjectName("label")
        self.txtUsername = QtWidgets.QLineEdit(self.centralwidget)
        self.txtUsername.setGeometry(QtCore.QRect(140, 200, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.txtUsername.setFont(font)
        self.txtUsername.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                       "border:2px solid rgba(0, 0, 0, 0);\n"
                                       "border-bottom-color: rgba(46, 82, 101, 255);\n"
                                       "color:rgb(0, 0, 0, 200);\n"
                                       "padding-bottom:7px;")
        self.txtUsername.setObjectName("txtUsername")
        self.txtPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPassword.setGeometry(QtCore.QRect(140, 280, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.txtPassword.setFont(font)
        self.txtPassword.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                       "border:2px solid rgba(0, 0, 0, 0);\n"
                                       "border-bottom-color: rgba(46, 82, 101, 255);\n"
                                       "color:rgb(0, 0, 0, 200);\n"
                                       "padding-bottom:7px;")
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setObjectName("txtPassword")
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(160, 360, 201, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
 #       brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(68, 23, 23))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
  #      brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
 #       brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(68, 23, 23))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(68, 23, 23))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
  #      brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
 #       brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(68, 23, 23))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
   #     brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
  #      brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(68, 23, 23))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(68, 23, 23))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
  #      brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
  #      brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(68, 23, 23))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
  #      brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
   #     brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(68, 23, 23))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(68, 23, 23))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
 #       brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.Highlight, brush)
        self.btnLogin.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnLogin.setFont(font)
        self.btnLogin.setMouseTracking(True)
        self.btnLogin.setTabletTracking(True)
        self.btnLogin.setAcceptDrops(False)
        self.btnLogin.setStyleSheet("")
        self.btnLogin.setObjectName("btnLogin")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 50, 391, 411))
        self.label_6.setStyleSheet("background-color: rgb(135, 0, 0);\n"
                                   "border-radius: 50px;\n"
                                   "border-top-right-radius: 50px;\n"
                                   "\n"
                                   "")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_6.raise_()
        self.label_5.raise_()
        self.label.raise_()
        self.txtUsername.raise_()
        self.txtPassword.raise_()
        self.btnLogin.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Event ketika tombol di klik
        self.btnLogin.clicked.connect(self.login)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">LOGIN</span></p></body></html>"))
        self.txtUsername.setPlaceholderText(
            _translate("MainWindow", "Username"))
        self.txtPassword.setPlaceholderText(
            _translate("MainWindow", "Password"))
        self.btnLogin.setText(_translate("MainWindow", "LOGIN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
