#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os.path
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
 
class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        HERE = os.path.dirname(os.path.abspath(__file__))
        UI = os.path.join(HERE, 'talker.ui')
        self.ui = QUiLoader().load(UI)
        self.setCentralWidget(self.ui)
        self.ui.lineEdit.returnPressed.connect(self.returnPressed)
        
    def returnPressed(self):
        print(self.ui.lineEdit.text())
 
 
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    a = MyWindow()
    a.show()
    sys.exit(app.exec_())
 
