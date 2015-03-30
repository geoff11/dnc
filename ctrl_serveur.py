import sys.os.os.path
from socket import *

# Jaune 1 Team -- DNC Server  

# -*- coding: utf-8 -*- 
from socket import *
from datetime import *
import sys
#import chat

if len(sys.argv) != 2 :
    print("Usage: {} <port>".format(sys.argv[0]))
    sys.exit(1)

TAILLE_TAMPON = 256

# Ouverture en ecriture du fichier de log
logs = open("serveur.log", "w")
    
maSock = socket(AF_INET,SOCK_DGRAM)
maSock.bind(('',int(sys.argv[1])))
print("Serveur en attente sur le port {} .".format(sys.argv[1],), file=logs)  # Ecriture du fichier de log 

while True:
    try:
        # Recuperation de la requete du client
        requete = maSock.recvfrom(TAILLE_TAMPON)
        
        # Extraction du message et de l adresse sur le client
        (mess, adr_client) = requete
        ip_client, port_client = adr_client

        message = mess.decode().lower()
        
        
        print("Requete provenant de {}. Longueur = {}". \
        format(ip_client, len(mess)), file=logs)      # Ecriture du fichier de log 
        
        
        # Construction de la reponse
        
        if message == "sleep":
            reponse = self.sleep()
        elif message == "list":
            reponse = self.list()
        elif message == "quit":
            reponse = self.quit()
        elif message == "wake":
            reponse = self.wake()
        elif message == "logchange":
            reponse = self.logchange()
        elif message == "private":
            reponse = self.private()
        elif message == "acceptpc":
            reponse = self.acceptpc()
        elif message == "denypc":
            reponse = self.denypc()
        elif message == "stoppc":
            reponse = self.stoppc()
        elif message == "filesend":
            reponse = self.filesend()
        elif message == "fileacc":
            reponse = self.fileacc()
        elif message == "fileden":
            reponse = self.fileden()
        
        # Envoi de la reponse au client
        maSock.sendto(reponse.encode(), adr_client)
        
    except KeyboardInterrupt: break
    
maSock.close()
print("Arret du serveur", file=logs)
logs.close() 
sys.exit(0)