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

chat = chat() # création du chat

while True:
    try:
        # Recuperation de la requete du client
        requete = maSock.recvfrom(TAILLE_TAMPON)
        
        # Extraction du message, de l adresse et du pseudo sur le client
        (mess, adr_client, pseudo) = requete
        ip_client, port_client = adr_client
        user = chat.identifierClient(adr_client, pseudo)

        message = mess.decode().lower().split() # on découpe le message en tableau de mots
        cmd = message[0]
        
        
        print("Requete provenant de {}. Longueur = {}". \
        format(ip_client, len(mess)), file=logs)      # Ecriture du fichier de log   
        
        # Construction de la reponse
        
        
        if cmd == "sleep":
            reponse = user.sleep()
        elif cmd == "list":
            reponse = user.list()
        elif cmd == "quit":
            reponse = user.quit()
        elif cmd == "wake":
            reponse = user.wake()
        elif cmd == "logchange":
            reponse = user.logchange()
        elif cmd ==  "private":
            reponse = user.private()
        elif cmd == "acceptpc":
            reponse = user.acceptpc()
        elif cmd == "denypc":
            reponse = user.denypc()
        elif cmd == "stoppc":
            reponse = user.stoppc()
        elif cmd == "filesend":
            reponse = user.filesend()
        elif cmd == "fileacc":
            reponse = user.fileacc()
        elif cmd == "fileden":
            reponse = user.fileden()
        
        # Envoi de la reponse au client
        maSock.sendto(reponse.encode(), adr_client)
        
    except KeyboardInterrupt: break
    
maSock.close()
print("Arret du serveur", file=logs)
logs.close() 
sys.exit(0)