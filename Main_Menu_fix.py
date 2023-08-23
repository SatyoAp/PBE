from PyQt5 import QtCore, QtGui, QtWidgets
from DataWarga_fix import datawarga
from Laporan_fix import laporan


class main_utama(object):
    def tampil_datawarga(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = datawarga()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def tampil_laporan(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = laporan()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(544, 459)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 20, 351, 131))
        self.label.setObjectName("label")
        self.btnDataWarga = QtWidgets.QPushButton(self.centralwidget)
        self.btnDataWarga.setGeometry(QtCore.QRect(200, 180, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnDataWarga.setFont(font)
        self.btnDataWarga.setObjectName("btnDataWarga")
        self.btnLaporan = QtWidgets.QPushButton(self.centralwidget)
        self.btnLaporan.setGeometry(QtCore.QRect(200, 260, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnLaporan.setFont(font)
        self.btnLaporan.setObjectName("btnLaporan")
        self.btnClose = QtWidgets.QPushButton(self.centralwidget)
        self.btnClose.setGeometry(QtCore.QRect(240, 370, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnClose.setFont(font)
        self.btnClose.setObjectName("btnClose")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 10, 491, 421))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "border-radius: 50px;\n"
                                   "border-top-right-radius: 50px;\n"
                                   "\n"
                                   "")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 0, 511, 441))
        self.label_8.setStyleSheet("background-color: rgb(145, 0, 0);\n"
                                   "border-radius: 50px;\n"
                                   "border-top-right-radius: 50px;\n"
                                   "\n"
                                   "")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_8.raise_()
        self.label_7.raise_()
        self.label.raise_()
        self.btnDataWarga.raise_()
        self.btnLaporan.raise_()
        self.btnClose.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Event Ketika tombol di klik
        self.btnDataWarga.clicked.connect(self.tampil_datawarga)
        self.btnLaporan.clicked.connect(self.tampil_laporan)
        self.btnClose.clicked.connect(MainWindow.close)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Aplikasi Jimpitan Warga</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Desa Tambaksogra RT 06 / 02</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Sumbang, Banyumas</span></p></body></html>"))
        self.btnDataWarga.setText(_translate("MainWindow", "Data Jimpitan"))
        self.btnLaporan.setText(_translate("MainWindow", "Laporan"))
        self.btnClose.setText(_translate("MainWindow", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = main_utama()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
