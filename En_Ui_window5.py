# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'databaseinterface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1136, 446)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loadDB = QtWidgets.QPushButton(self.centralwidget)
        self.loadDB.setGeometry(QtCore.QRect(530, 360, 101, 31))
        self.loadDB.setObjectName("loadDB")
        self.edit = QtWidgets.QPushButton(self.centralwidget)
        self.edit.setGeometry(QtCore.QRect(310, 360, 91, 31))
        self.edit.setObjectName("edit")
        self.table111 = QtWidgets.QTableWidget(self.centralwidget)
        self.table111.setGeometry(QtCore.QRect(15, 11, 1101, 291))
        self.table111.setObjectName("table111")
        self.table111.setColumnCount(11)
        self.table111.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table111.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table111.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table111.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table111.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table111.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table111.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table111.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table111.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table111.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table111.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table111.setHorizontalHeaderItem(10, item)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 320, 281, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.new_win = QtWidgets.QPushButton(self.layoutWidget)
        self.new_win.setObjectName("new_win")
        self.horizontalLayout.addWidget(self.new_win)
        self.name_patient = QtWidgets.QLineEdit(self.layoutWidget)
        self.name_patient.setObjectName("name_patient")
        self.horizontalLayout.addWidget(self.name_patient)
        self.register_butt = QtWidgets.QPushButton(self.centralwidget)
        self.register_butt.setGeometry(QtCore.QRect(810, 330, 101, 41))
        self.register_butt.setObjectName("register_butt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1136, 21))
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
        self.loadDB.setText(_translate("MainWindow", "load"))
        self.edit.setText(_translate("MainWindow", "edit"))
        item = self.table111.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.table111.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.table111.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Surname"))
        item = self.table111.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Gender"))
        item = self.table111.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Father"))
        item = self.table111.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Telephone"))
        item = self.table111.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "City"))
        item = self.table111.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Street"))
        item = self.table111.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Nationality"))
        item = self.table111.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Passport"))
        item = self.table111.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Age"))
        self.new_win.setText(_translate("MainWindow", "patient data "))
        self.register_butt.setText(_translate("MainWindow", "register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
