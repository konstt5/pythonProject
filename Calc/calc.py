# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(272, 360)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.result_label = QtWidgets.QLabel(self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(0, 0, 271, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.result_label.setFont(font)
        self.result_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.result_label.setFrameShape(QtWidgets.QFrame.Box)
        self.result_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.result_label.setObjectName("result_label")
        self.btn7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn7.setGeometry(QtCore.QRect(0, 40, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn7.setFont(font)
        self.btn7.setAutoFillBackground(False)
        self.btn7.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.btn7.setCheckable(False)
        self.btn7.setDefault(False)
        self.btn7.setFlat(False)
        self.btn7.setObjectName("btn7")
        self.btn8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn8.setGeometry(QtCore.QRect(90, 40, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn8.setFont(font)
        self.btn8.setAutoFillBackground(False)
        self.btn8.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.btn8.setCheckable(False)
        self.btn8.setDefault(False)
        self.btn8.setFlat(False)
        self.btn8.setObjectName("btn8")
        self.btn9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn9.setGeometry(QtCore.QRect(180, 40, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn9.setFont(font)
        self.btn9.setAutoFillBackground(False)
        self.btn9.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.btn9.setCheckable(False)
        self.btn9.setDefault(False)
        self.btn9.setFlat(False)
        self.btn9.setObjectName("btn9")
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(0, 120, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn4.setFont(font)
        self.btn4.setAutoFillBackground(False)
        self.btn4.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.btn4.setCheckable(False)
        self.btn4.setDefault(False)
        self.btn4.setFlat(False)
        self.btn4.setObjectName("btn4")
        self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn5.setGeometry(QtCore.QRect(90, 120, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn5.setFont(font)
        self.btn5.setAutoFillBackground(False)
        self.btn5.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.btn5.setCheckable(False)
        self.btn5.setDefault(False)
        self.btn5.setFlat(False)
        self.btn5.setObjectName("btn5")
        self.btn6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn6.setGeometry(QtCore.QRect(180, 120, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn6.setFont(font)
        self.btn6.setAutoFillBackground(False)
        self.btn6.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.btn6.setCheckable(False)
        self.btn6.setDefault(False)
        self.btn6.setFlat(False)
        self.btn6.setObjectName("btn6")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(0, 200, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn1.setFont(font)
        self.btn1.setAutoFillBackground(False)
        self.btn1.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.btn1.setCheckable(False)
        self.btn1.setDefault(False)
        self.btn1.setFlat(False)
        self.btn1.setObjectName("btn1")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(90, 200, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn2.setFont(font)
        self.btn2.setAutoFillBackground(False)
        self.btn2.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.btn2.setCheckable(False)
        self.btn2.setDefault(False)
        self.btn2.setFlat(False)
        self.btn2.setObjectName("btn2")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(180, 200, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn3.setFont(font)
        self.btn3.setAutoFillBackground(False)
        self.btn3.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.btn3.setCheckable(False)
        self.btn3.setDefault(False)
        self.btn3.setFlat(False)
        self.btn3.setObjectName("btn3")
        self.btn0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn0.setGeometry(QtCore.QRect(0, 280, 141, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn0.setFont(font)
        self.btn0.setAutoFillBackground(False)
        self.btn0.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.btn0.setCheckable(False)
        self.btn0.setDefault(False)
        self.btn0.setFlat(False)
        self.btn0.setObjectName("btn0")
        self.btnEq = QtWidgets.QPushButton(self.centralwidget)
        self.btnEq.setGeometry(QtCore.QRect(140, 280, 131, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnEq.setFont(font)
        self.btnEq.setAutoFillBackground(False)
        self.btnEq.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.btnEq.setCheckable(False)
        self.btnEq.setDefault(False)
        self.btnEq.setFlat(False)
        self.btnEq.setObjectName("btnEq")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.result_label.setText(_translate("MainWindow", "0"))
        self.btn7.setText(_translate("MainWindow", "7"))
        self.btn8.setText(_translate("MainWindow", "8"))
        self.btn9.setText(_translate("MainWindow", "9"))
        self.btn4.setText(_translate("MainWindow", "4"))
        self.btn5.setText(_translate("MainWindow", "5"))
        self.btn6.setText(_translate("MainWindow", "6"))
        self.btn1.setText(_translate("MainWindow", "1"))
        self.btn2.setText(_translate("MainWindow", "2"))
        self.btn3.setText(_translate("MainWindow", "3"))
        self.btn0.setText(_translate("MainWindow", "0"))
        self.btnEq.setText(_translate("MainWindow", "="))

    def add_functions(self):
        self.btn0.clicked.connect(lambda: self.write_number(self.btn0.text()))
        self.btn1.clicked.connect(lambda: self.write_number(self.btn1.text()))
        self.btn2.clicked.connect(lambda: self.write_number(self.btn2.text()))
        self.btn3.clicked.connect(lambda: self.write_number(self.btn3.text()))
        self.btn4.clicked.connect(lambda: self.write_number(self.btn4.text()))
        self.btn5.clicked.connect(lambda: self.write_number(self.btn5.text()))
        self.btn6.clicked.connect(lambda: self.write_number(self.btn6.text()))
        self.btn7.clicked.connect(lambda: self.write_number(self.btn7.text()))
        self.btn8.clicked.connect(lambda: self.write_number(self.btn8.text()))
        self.btn9.clicked.connect(lambda: self.write_number(self.btn9.text()))
        self.btnEq.clicked.connect(lambda: self.write_number(self.btnEq.text()))

    def write_number(self, number):
        if number == "=":
            mess = QMessageBox()
            mess.setWindowTitle("Ошибка")
            mess.setText("Вы нажали =")
            mess.setIcon(QMessageBox.Warning)
            mess.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            mess.setInformativeText("дополнительная информация")
            mess.setDetailedText("Подробное описание ошибки")

            mess.exec_()
        elif self.result_label.text() != "0":
            self.result_label.setText(self.result_label.text() + number)
        else:
            self.result_label.setText(number)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
