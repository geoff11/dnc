import sys.os.os.path
from socket import *

# Jaune 1 Team -- DNC Server  

# -*- coding: utf-8 -*- 
from socket import *
from datetime import *
import sys
import chat

if len(sys.argv) != 2 :
    print("Usage: {} <port>".format(sys.argv[0]))
    sys.exit(1)

TAILLE_TAMPON = 256

# Ouverture en ecriture du fichier de log
logs = open("serveur.log", "w")
    
maSock = socket(AF_INET,SOCK_DGRAM)
maSock.bind(('',int(sys.argv[1])))
print("Serveur en attente sur le port {} .".format(sys.argv[1],), file=logs)  # Ecriture du fichier de log 
c = chat()

while True:
    try:
        # Recuperation de la requete du client
        requete = maSock.recvfrom(TAILLE_TAMPON)
        
        # Extraction du message, de l adresse et du pseudo sur le client
        (mess, adr_client, pseudo) = requete
        ip_client, port_client = adr_client
        c.identifierClient(adr_client, pseudo)

        message = mess.decode().lower()
        
        
        print("Requete provenant de {}. Longueur = {}". \
        format(ip_client, len(mess)), file=logs)      # Ecriture du fichier de log 
        
        
        # Construction de la reponse
        message = 
        
        
        if message == "sleep":
            reponse = c.sleep()
        elif message == "list":
            reponse = c.list()
        elif message == "quit":
            reponse = c.quit()
        elif message == "wake":
            reponse = c.wake()
        elif message == "logchange":
            reponse = c.logchange()
        elif message.contains  "private":
            reponse = c.private()
        elif message == "acceptpc":
            reponse = c.acceptpc()
        elif message == "denypc":
            reponse = c.denypc()
        elif message == "stoppc":
            reponse = c.stoppc()
        elif message == "filesend":
            reponse = c.filesend()
        elif message == "fileacc":
            reponse = c.fileacc()
        elif message == "fileden":
            reponse = c.fileden()
        
        # Envoi de la reponse au client
        maSock.sendto(reponse.encode(), adr_client)
        
    except KeyboardInterrupt: break
    
maSock.close()
print("Arret du serveur", file=logs)
logs.close() 
sys.exit(0)