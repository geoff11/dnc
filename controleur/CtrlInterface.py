from PyQt4 import QtCore, QtGui
from PyQt4.Qt import *
from vue import FenClient
import time, sys, logging

class CtrlInterface(QWidget):
    
    def __init__(self):
        
        QWidget.__init__(self)
        self.fenPrincipale = QMainWindow()
        self.bufferInput= "" # Buffer de l'entree standard du client (saisie des commandes)
        self.state = False
        self.host = ""
        self.port = ""
        
        self.ui1 = FenClient.Ui_FenClient()
        self.ui1.setupUi(self.fenPrincipale)
        self.ui1.btnEnvoyer.clicked.connect(self.sendMess)
        self.ui1.message.returnPressed.connect(self.sendMess) # touche enter
        
        
    
    def iniFenPrincipale(self):
        self.fenPrincipale.show()
            
    def getState(self):
        return self.state
        
    def maj(self): #maj des encadres user, mais trouver une solution pour intercepter l objet chat...
        pass
    
    def sendMess(self):
        cmd = self.ui1.message.text()
        self.ui1.message.clear()
        self.bufferInput = cmd
        self.state = True
        
    def printConsole(self, msg):
        self.ui1.ecranMain.append(msg)
        logging.basicConfig(level=logging.DEBUG, filename="logfile.log", filemode="a+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")
        logging.info(msg)
        
    def clearConsole(self):
        self.ui1.ecranMain.clear()
        
    def setPseudo(self, pseudo):
        self.ui1.pseudo = pseudo
    
    def setPort(self, port):
        self.ui1.serveurPort = port
        self.port = port
    
    def setHost(self, host):
        self.ui1.serveurIP = host
        self.host = host
    
    def getPort(self):
        return self.port
    
    def getHost(self):
        return self.host
    
    def getAllCompleted(self):
        return (self.host != "" and self.port != "")
        