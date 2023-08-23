from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import sys
con = sqlite3.connect("dbjimpitan.db")
cur = con.cursor()


class datawarga(object):
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

    def clear_data(self):
        no_warga = self.txtNo.setText("")
        nama = self.txtNama.setText("")
        tahun = self.txtTahun.setText("")
        bulan = self.cbBulan.setCurrentIndex(0)
        tanggal = self.dateEdit_2.setText("")
        nominal = self.txtNominal.setText("")

    def save_data(self):
        no_warga = self.txtNo.text()  # Definisikan Masing masing line edit
        nama = self.txtNama.text()
        tahun = self.txtTahun.text()
        bulan = self.cbBulan.currentText()
        tanggal = self.dateEdit_2.text()
        nominal = self.txtNominal.text()

        if(no_warga and nama and tahun and bulan and tanggal and nominal != ""):
            query = "INSERT INTO tbdatajimpitan(no_warga,nama,tahun,bulan,tanggal,nominal) VALUES(?,?,?,?,?,?)"
            form = (no_warga, nama, tahun,
                    bulan, tanggal, nominal)
            data = cur.execute(query, form)
            if(data):
                self.messageBox("Sukses", "Berhasil Simpan Data Jimpitan")
                self.clear_data()
                self.loaddata()
                con.commit()
            else:
                self.warningBox("WARNING !!", "Data Gagal Di Simpan")

        else:
            self.warningBox("WARNING !!", "Data tidak boleh kosong")

    def update_data(self):
        no_warga = self.txtNo.text()
        nama = self.txtNama.text()
        tahun = self.txtTahun.text()
        bulan = self.cbBulan.currentText()
        tanggal = self.dateEdit_2.text()
        nominal = self.txtNominal.text()

        if(no_warga and nama and tahun and bulan and tanggal and nominal != ""):
            query = "UPDATE tbdatajimpitan SET nama=?, tahun=?, bulan=?, tanggal=?, nominal=? WHERE no_warga=?"
            form = (nama, tahun, bulan,
                    tanggal, nominal, no_warga)

            data = cur.execute(query, form)
            if(data):
                self.messageBox("Berhasil", "Berhasil Update Data")
                self.clear_data()
                self.loaddata()
            else:
                self.warningBox("Gagal", "Data Gagal Di Update")
            con.commit()
        else:
            self.warningBox("Eror", "Data tidak boleh kosong")

    def delete_data(self):
        no_warga = self.txtNo.text()
        if(no_warga != ""):
            query = "DELETE FROM tbdatajimpitan WHERE no_warga=?"
            data = cur.execute(query, (no_warga,))
            if(data):
                self.messageBox("Berhasil", "Berhasil Delete Data")
                self.loaddata()
                self.clear_data()
            else:
                self.warningBox("Gagal", "Data gagal Di Hapus")
            con.commit()
        else:
            self.warningBox("Eror", "Gagal hapus data")

    def loaddata(self):
        cur.execute("SELECT * FROM tbdatajimpitan order by no_warga asc")
        result = cur.fetchall()
        column = 0  # menefinisikan data setiap kolom dalam satu baris supaya tercetak pada row
        row = 0     # mendefinisikan baris yang terbentuk tetapi belum tercetak datanya
        self.tableWidget.setRowCount(len(result))
        for tabel in result:
            self.tableWidget.setItem(
                column, 0, QtWidgets.QTableWidgetItem(str(tabel[0])))
            self.tableWidget.setItem(
                column, 1, QtWidgets.QTableWidgetItem(tabel[1]))
            self.tableWidget.setItem(
                column, 2, QtWidgets.QTableWidgetItem(str(tabel[2])))
            self.tableWidget.setItem(
                column, 3, QtWidgets.QTableWidgetItem(tabel[3]))
            self.tableWidget.setItem(
                column, 4, QtWidgets.QTableWidgetItem(str(tabel[4])))
            self.tableWidget.setItem(
                column, 5, QtWidgets.QTableWidgetItem(str(tabel[5])))
            row += 1
            column += 1

    def getItem(self):  # Merupakan event mouse klik
        column = self.tableWidget.currentRow()
        columnItemNoWarga = self.tableWidget.item(column, 0).text()
        columnItemNama = self.tableWidget.item(column, 1).text()
        columnItemTahun = self.tableWidget.item(column, 2).text()
        columnItemBulan = self.tableWidget.item(column, 3).text()
        columnItemTanggal = self.tableWidget.item(column, 4).text()
        columnItemNominal = self.tableWidget.item(column, 5).text()

        self.txtNo.setText(columnItemNoWarga)
        self.txtNama.setText(columnItemNama)
        self.txtTahun.setText(columnItemTahun)
        self.cbBulan.setCurrentText(columnItemBulan)
        self.dateEdit_2.setText(columnItemTanggal)
        self.txtNominal.setText(columnItemNominal)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(590, 60, 131, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnSave = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnSave.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnSave.setFont(font)
        self.btnSave.setObjectName("btnSave")
        self.verticalLayout.addWidget(self.btnSave)
        self.btnUpdate = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnUpdate.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnUpdate.setFont(font)
        self.btnUpdate.setObjectName("btnUpdate")
        self.verticalLayout.addWidget(self.btnUpdate)
        self.btnDelete = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnDelete.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnDelete.setFont(font)
        self.btnDelete.setObjectName("btnDelete")
        self.verticalLayout.addWidget(self.btnDelete)
        self.btnClear = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnClear.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnClear.setFont(font)
        self.btnClear.setObjectName("btnClear")
        self.verticalLayout.addWidget(self.btnClear)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(330, 20, 181, 41))
        self.label_6.setObjectName("label_6")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 70, 481, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
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
        self.gridLayout.addWidget(self.cbBulan, 3, 2, 1, 1)
        self.txtNama = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtNama.setObjectName("txtNama")
        self.gridLayout.addWidget(self.txtNama, 1, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.txtNo = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtNo.setObjectName("txtNo")
        self.gridLayout.addWidget(self.txtNo, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.txtTahun = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtTahun.setObjectName("txtTahun")
        self.gridLayout.addWidget(self.txtTahun, 2, 2, 1, 1)
        self.txtNominal = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtNominal.setObjectName("txtNominal")
        self.gridLayout.addWidget(self.txtNominal, 5, 2, 1, 1)
        self.dateEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.gridLayout.addWidget(self.dateEdit_2, 4, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 290, 611, 251))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed | QtWidgets.QAbstractItemView.DoubleClicked |
                                         QtWidgets.QAbstractItemView.EditKeyPressed | QtWidgets.QAbstractItemView.SelectedClicked)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.btnClose = QtWidgets.QPushButton(self.centralwidget)
        self.btnClose.setGeometry(QtCore.QRect(680, 509, 81, 31))
        self.btnClose.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnClose.setFont(font)
        self.btnClose.setObjectName("btnClose")
        self.btnLoad = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoad.setGeometry(QtCore.QRect(50, 250, 129, 30))
        self.btnLoad.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnLoad.setFont(font)
        self.btnLoad.setObjectName("btnLoad")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(0, 10, 791, 571))
        self.label_8.setStyleSheet("background-color: rgb(140, 0, 0);\n"
                                   "border-radius: 50px;\n"
                                   "border-top-right-radius: 50px;\n"
                                   "\n"
                                   "")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 20, 771, 551))
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "border-radius: 50px;\n"
                                   "border-top-right-radius: 50px;\n"
                                   "\n"
                                   "")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_8.raise_()
        self.label_9.raise_()
        self.verticalLayoutWidget.raise_()
        self.label_6.raise_()
        self.gridLayoutWidget.raise_()
        self.tableWidget.raise_()
        self.btnClose.raise_()
        self.btnLoad.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Event ketika tombol di klik
        self.btnSave.clicked.connect(self.save_data)
        self.btnUpdate.clicked.connect(self.update_data)
        self.btnDelete.clicked.connect(self.delete_data)
        self.btnClear.clicked.connect(self.clear_data)
        self.tableWidget.clicked.connect(self.getItem)
        self.btnLoad.clicked.connect(self.loaddata)
        self.btnClose.clicked.connect(MainWindow.close)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnSave.setText(_translate("MainWindow", "Save"))
        self.btnUpdate.setText(_translate("MainWindow", "Update"))
        self.btnDelete.setText(_translate("MainWindow", "Delete"))
        self.btnClear.setText(_translate("MainWindow", "Clear"))
        self.label_6.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Data Jimpitan</span></p></body></html>"))
        self.label.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Bulan</span></p></body></html>"))
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
        self.label_7.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Tahun</span></p></body></html>"))
        self.label_3.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Nama</span></p></body></html>"))
        self.label_2.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">No Warga</span></p></body></html>"))
        self.label_4.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Tanggal</span></p></body></html>"))
        self.label_5.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Nominal</span></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "No Warga"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nama"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tahun"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Bulan"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Tanggal"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Nominal"))
        self.btnClose.setText(_translate("MainWindow", "Close"))
        self.btnLoad.setText(_translate("MainWindow", "Load"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = datawarga()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
