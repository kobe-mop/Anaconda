# -*- coding: utf-8 -*-

"""
Module implementing HelloWindows.
"""
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog,  QApplication

from Ui_HelloWindows import Ui_Dialog


class HelloWindows(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(HelloWindows, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_Button_OK_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.label.setText('这是我的第一个PyQt5 程序')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = HelloWindows()
    dlg.show()
    sys.exit(app.exec_())
