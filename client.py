import socket, sys, threading
#from PyQt4 import QtCore,QtGui     #  Uniquement pour version graphique
#from controleur import CtrlInterface
import sys
# Jaune 1 Team -- DNC Client 
   
# Définition d'un client réseau gérant en parallèle l'émission
# et la réception des messages (utilisation de 2 THREADS).


class Thread_Reception(threading.Thread):
    '''
        Classe ThreadReception = objet thread gérant la réception des messages
    '''
    
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn           # réf. du socket de connexion
        
   
    def run(self):
        #print(welcoming)
        print("Login : ")
        
        while True:
            recu = self.connexion.recv(TAILLE_TAMPON).decode()
            message = recu.lower().split() # on découpe le message en tableau de mots
            if message[0] == "/quit": # A Mon avis la on est pas loin du fuck a resoudre 
                print("logout successful")
                self.connexion.close()
                break
            else:
                print ("*" + recu + "*")
        
        
            
class Thread_Emission(threading.Thread):
    
    '''
        Classe ThreadEmission = objet thread gérant l'émission des messages
    '''
    
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn           # réf. du socket de connexion
   
    def run(self):
        while 1:
            message_emis = input()
            self.connexion.send(message_emis.encode())
            
 
 
 
 
if __name__ == '__main__':           
    # Programme principal - Établissement de la connexion par socket :
    
    if len(sys.argv) != 3:
        print("Usage: {} <ip> <port>".format(sys.argv[0]))
        sys.exit(1)

    TAILLE_TAMPON = 1024
    
    
    ''' Lancement de la socket '''
    connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = sys.argv[1]
    port = int(sys.argv[2])
    
    try:
        connexion.connect((host, port))
    except socket.error:
        print ("Connexion failed")
        sys.exit()
    
    print ("Connexion OK")
            
    # Dialogue avec le serveur : on lance deux threads pour gérer
    # indépendamment l'émission et la réception des messages :
    th_E = Thread_Emission(connexion)
    th_R = Thread_Reception(connexion)
    th_E.start()
    th_R.start()
    
    
    ''' Lancement interface '''
    '''
    app = QtGui.QApplication(["DNC"])
    appli = CtrlInterface.CtrlInterface()
    appli.iniFenPrincipale()
    r = app.exec_()
    '''
    