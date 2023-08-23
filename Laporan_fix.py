from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import sys


class laporan(object):
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

    def tampil_data(self):
        tahun = self.cbTahun.currentText()  # Mendefinisikan comboBox
        bulan = self.cbBulan.currentText()
        if (tahun and bulan != "--- PILIH ---"):
            # Membuat variabel untuk memanggil database
            con = sqlite3.connect("dbjimpitan.db")
            cur = con.cursor()  # Membuat variabel untuk memanggil koneksi
            cur.execute(
                "SELECT * FROM tbdatajimpitan WHERE  tahun=? AND bulan=?", (tahun, bulan))
            result = cur.fetchall()
            if result:
                column = 0  # Data yang tercetak dalam satu baris
                row = 0     # Baris yang terbuat tetapi belum ada datanya
                self.tbLaporan.setRowCount(len(result))
                for tabel in result:
                    self.tbLaporan.setItem(
                        column, 0, QtWidgets.QTableWidgetItem(str(tabel[0])))
                    self.tbLaporan.setItem(
                        column, 1, QtWidgets.QTableWidgetItem(tabel[1]))
                    self.tbLaporan.setItem(
                        column, 2, QtWidgets.QTableWidgetItem(str(tabel[2])))
                    self.tbLaporan.setItem(
                        column, 3, QtWidgets.QTableWidgetItem(tabel[3]))
                    self.tbLaporan.setItem(
                        column, 4, QtWidgets.QTableWidgetItem(str(tabel[4])))
                    self.tbLaporan.setItem(
                        column, 5, QtWidgets.QTableWidgetItem(str(tabel[5])))
                    row += 1
                    column += 1
            else:
                self.warningBox("Upps", "Data tidak ditemukan")
            con.close()
        else:
            self.warningBox("Gagal", "Pilih Tahun dan Bulan Dahulu")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(699, 512)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 30, 201, 41))
        self.label.setObjectName("label")
        self.btnTampil = QtWidgets.QPushButton(self.centralwidget)
        self.btnTampil.setGeometry(QtCore.QRect(560, 120, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnTampil.setFont(font)
        self.btnTampil.setObjectName("btnTampil")
        self.tbLaporan = QtWidgets.QTableWidget(self.centralwidget)
        self.tbLaporan.setGeometry(QtCore.QRect(60, 190, 601, 231))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tbLaporan.setFont(font)
        self.tbLaporan.setObjectName("tbLaporan")
        self.tbLaporan.setColumnCount(6)
        self.tbLaporan.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbLaporan.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbLaporan.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbLaporan.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbLaporan.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbLaporan.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbLaporan.setHorizontalHeaderItem(5, item)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 100, 451, 71))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.cbBulan = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.cbBulan.setObjectName("cbBulan")
        self.cbBulan.addItem("")
        self.cbBulan.addItem("")
        self.cbBulan.addItem("")
        self.cbBulan.addItem("")
        self.cbBulan.addItem("")
        self.cbBulan.addItem("")
        self.cbBulan.addItem("")
        self.cbBulan.addItem("")
        self.cbBulan.addItem("")
        self.cbBulan.addItem("")
        self.cbBulan.addItem("")
        self.cbBulan.addItem("")
        self.cbBulan.addItem("")
        self.gridLayout.addWidget(self.cbBulan, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.cbTahun = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.cbTahun.setObjectName("cbTahun")
        self.cbTahun.addItem("")
        self.cbTahun.addItem("")
        self.cbTahun.addItem("")
        self.cbTahun.addItem("")
        self.cbTahun.addItem("")
        self.cbTahun.addItem("")
        self.gridLayout.addWidget(self.cbTahun, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.btnClose = QtWidgets.QPushButton(self.centralwidget)
        self.btnClose.setGeometry(QtCore.QRect(570, 450, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnClose.setFont(font)
        self.btnClose.setObjectName("btnClose")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 10, 671, 501))
        self.label_8.setStyleSheet("background-color: rgb(140, 0, 0);\n"
                                   "border-radius: 50px;\n"
                                   "border-top-right-radius: 50px;\n"
                                   "\n"
                                   "")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 20, 651, 481))
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "border-radius: 50px;\n"
                                   "border-top-right-radius: 50px;\n"
                                   "\n"
                                   "")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_8.raise_()
        self.label_9.raise_()
        self.label.raise_()
        self.btnTampil.raise_()
        self.tbLaporan.raise_()
        self.gridLayoutWidget.raise_()
        self.btnClose.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Event ketika tombol di klik
        self.btnTampil.clicked.connect(self.tampil_data)
        self.btnClose.clicked.connect(MainWindow.close)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Laporan Jimpitan</span></p></body></html>"))
        self.btnTampil.setText(_translate("MainWindow", "Tampil"))
        item = self.tbLaporan.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "No Warga"))
        item = self.tbLaporan.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nama"))
        item = self.tbLaporan.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tahun"))
        item = self.tbLaporan.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Bulan"))
        item = self.tbLaporan.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Tanggal"))
        item = self.tbLaporan.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Nominal"))
        self.cbBulan.setItemText(0, _translate("MainWindow", "--- PILIH ---"))
        self.cbBulan.setItemText(1, _translate("MainWindow", "Januari"))
        self.cbBulan.setItemText(2, _translate("MainWindow", "Februari"))
        self.cbBulan.setItemText(3, _translate("MainWindow", "Maret"))
        self.cbBulan.setItemText(4, _translate("MainWindow", "April"))
        self.cbBulan.setItemText(5, _translate("MainWindow", "Mei"))
        self.cbBulan.setItemText(6, _translate("MainWindow", "Juni"))
        self.cbBulan.setItemText(7, _translate("MainWindow", "Juli"))
        self.cbBulan.setItemText(8, _translate("MainWindow", "Agustus"))
        self.cbBulan.setItemText(9, _translate("MainWindow", "September"))
        self.cbBulan.setItemText(10, _translate("MainWindow", "Oktober"))
        self.cbBulan.setItemText(11, _translate("MainWindow", "November"))
        self.cbBulan.setItemText(12, _translate("MainWindow", "Desember"))
        self.label_3.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Bulan</span></p></body></html>"))
        self.cbTahun.setItemText(0, _translate("MainWindow", "--- PILIH ---"))
        self.cbTahun.setItemText(1, _translate("MainWindow", "2023"))
        self.cbTahun.setItemText(2, _translate("MainWindow", "2024"))
        self.cbTahun.setItemText(3, _translate("MainWindow", "2025"))
        self.cbTahun.setItemText(4, _translate("MainWindow", "2026"))
        self.cbTahun.setItemText(5, _translate("MainWindow", "2027"))
        self.label_2.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Tahun</span></p></body></html>"))
        self.btnClose.setText(_translate("MainWindow", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = laporan()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
