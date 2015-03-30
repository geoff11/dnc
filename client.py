__author__ = 'think'
import os,sys,os.path
from socket import *

# Jaune 1 Team -- DNC Client 

# -*- coding: utf-8 -*- 
from socket import *
import sys

if len(sys.argv) != 3:
    print("Usage: {} <ip> <port>".format(sys.argv[0]))
    sys.exit(1)
    
TAILLE_TAMPON = 256


with socket(AF_INET, SOCK_DGRAM) as sock:
    while True : 
        mess = input("Entrez une commande (help pour la liste, quit pour quitter) : ")
        if mess.lower() == "quit": 
            break
        sock.sendto(mess.encode(), (sys.argv[1], int(sys.argv[2])))
        reponse, _ = sock.recvfrom(TAILLE_TAMPON)
        print("Réponse = " + reponse.decode())
    
sys.exit(0) # En cas de sortie de la boucle, fin du client. Normalement implicite 