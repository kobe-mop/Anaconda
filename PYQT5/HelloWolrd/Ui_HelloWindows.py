# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\shengxio\workspace\For_PYQT5\HelloWolrd\HelloWindows.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(520, 397)
        Dialog.setSizeGripEnabled(True)
        self.Button_OK = QtWidgets.QPushButton(Dialog)
        self.Button_OK.setGeometry(QtCore.QRect(70, 240, 93, 28))
        self.Button_OK.setObjectName("Button_OK")
        self.Button_Close = QtWidgets.QPushButton(Dialog)
        self.Button_Close.setGeometry(QtCore.QRect(320, 240, 93, 28))
        self.Button_Close.setObjectName("Button_Close")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 110, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.Button_Close.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Button_OK.setText(_translate("Dialog", "OK"))
        self.Button_Close.setText(_translate("Dialog", "Close"))
        self.label.setText(_translate("Dialog", "Display"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

