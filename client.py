import socket, sys, threading
from PyQt4 import QtCore,QtGui
from controleur import CtrlInterface
import sys

# Jaune 1 Team -- DNC Client 
   
# Définition d'un client réseau gérant en parallèle l'émission
# et la réception des messages (utilisation de 2 THREADS).


appli = "" # variable globale contenant les donnes de l appli

class Thread_Reception(threading.Thread):
    '''
        Classe ThreadReception = objet thread gérant la réception des messages
    '''
    
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn           # réf. du socket de connexion
   
    def run(self):
        appli.printConsole("Login please:")
        
        while True:
            recu = self.connexion.recv(TAILLE_TAMPON).decode()
                
            if recu == "* /quit *" :
                appli.printConsole("Logout successful")
                self.connexion.close()
                break
            else:
                appli.printConsole(recu)

            
        # Le thread <réception> se termine ici.
        # On force la fermeture du thread <émission> :
        #th_E._Thread__stop() # ne fonctionne pas
        
        appli.printConsole("Client stopped.")
        self.connexion.close()
        sys.exit() # il faut reussir a arreter le thread emission correctement pour que cette ligne fonctionne
        
            
class Thread_Emission(threading.Thread):
    
    '''
        Classe ThreadEmission = objet thread gérant l'émission des messages
    '''
    
    def __init__(self,conn):
        threading.Thread.__init__(self)
        self.connexion = conn   # réf. du socket de connexion
    
    def run(self):
        while 1 :
            if appli.getState():
                msg = appli.bufferInput.encode()
                self.connexion.send(msg)
                appli.bufferInput = ""
                appli.state = False
 
 
if __name__ == '__main__':           
    '''
    Programme principal - Établissement de la connexion par socket
    '''
    
    if len(sys.argv) != 3:
        print("Usage: {} <ip> <port>".format(sys.argv[0]))
        sys.exit(1)

    TAILLE_TAMPON = 1024
    
    ''' Lancement interface '''
    app = QtGui.QApplication(["DNC"])
    appli = CtrlInterface.CtrlInterface()
    appli.iniFenPrincipale()
    
    '''
    if len(sys.argv) == 3:
        appli.setHost(sys.argv[1])
        appli.setPort(int(sys.argv[2]))
        
    while True :
        if appli.getAllCompleted() :
            break
            
    port = appli.getPort()
    host = appli.getHost()
    '''
    
    host = sys.argv[1]
    port = int(sys.argv[2])
        
    ''' Lancement de la socket '''
    connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    
    try:
        connexion.connect((host, port))
    except socket.error:
        appli.printConsole("Connexion failed")
        sys.exit()
    
    appli.printConsole("Connexion OK")
            
    # Dialogue avec le serveur : on lance deux threads pour gérer
    # indépendamment l'émission et la réception des messages :
    th_E = Thread_Emission(connexion)
    th_R = Thread_Reception(connexion)
    th_E.start()
    th_R.start()
    
    r = app.exec_() # a mettre avant pour gerer port / host par interface, mais bloquant

    