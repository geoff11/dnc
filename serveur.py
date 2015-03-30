__author__ = 'think'
import sys.os.os.path
from socket import *

# Jaune 1 Team -- DNC Server  

# -*- coding: utf-8 -*- 
from socket import *
from datetime import *
import sys

if len(sys.argv) !=2 :
    print("Usage: {} <port>".format(sys.argv[0]))
    sys.exit(1)

TAILLE_TAMPON=256
# Tableaux de jours et mois pour affichage propre
JOURS = ['dimanche', 'lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi']
MOIS = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre',
        'octobre', 'novembre', 'décembre'] 

# Ouverture en ecriture du fichier de log
logs = open("serveur_date.log", "w")
    
maSock = socket(AF_INET,SOCK_DGRAM)
maSock.bind(('',int(sys.argv[1])))
print("Serveur en attente sur le port {} .".format(sys.argv[1],), file=logs)  # Ecriture du fichier de log 

while True:
    try:
        # Récupération de la requête du client
        requete = maSock.recvfrom(TAILLE_TAMPON)
        
        # Extraction du message et de l’adresse sur le client
        (mess, adr_client) = requete
        ip_client, port_client = adr_client

        message = mess.decode().lower()
        
        
        print("Requête provenant de {}. Longueur = {}". \
        format(ip_client, len(mess)), file=logs)      # Ecriture du fichier de log 
        
        # Construction de la réponse
        reponse = "100 "
        
        # Envoi de la réponse au client
        maSock.sendto(reponse.encode(), adr_client)
        
    except KeyboardInterrupt: break
    
maSock.close()
print("Arrêt du serveur", file=logs)
logs.close() 
sys.exit(0)