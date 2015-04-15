from PyQt4 import QtCore, QtGui
from PyQt4.Qt import *
from vue import FenClient
import time, sys

class CtrlInterface(QWidget):
    
    def __init__(self):
        
        QWidget.__init__(self)
        self.fenPrincipale=QMainWindow()
        #self.fenPrincipale=QWidget()
        self.ui1 = FenClient.Ui_FenClient()
        self.ui1.setupUi(self.fenPrincipale)
        
        
    def iniFenPrincipale(self):
        self.fenPrincipale.show()
        
        
    def maj(self):
        pass
        
   