'''
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


welcoming = """
                            #--/        \
                           |   \______   |
                             - ---^^- / /
                                     ||/
                                     |||
                                   .:'':.
                             /^/^^\/     \
                         0___O_\O_/       |
                         |               /
                         |       .._    /
                          \ ____/   |  |               /
                                    |  |             //
                             ^^^^^  |  |            ||
                          ^^^^^^^^^^|  \         __ /|
                         ^^^^^^   ^^|   \       /     \
                         ^^^^^    __|    \____/        |
WELCOME                    ^^^    \    /               |
TO                                 \-/          (_     \
DNC                                  |  |\__________\   |
                                    /|  |          \ \  |
                            _____  | |  |     ______\ \  \
                           /    ____/   |    /    ____/   \
                           \(_ /         \   \(_ /        |
                               \_(____.../       \_(_____/"""


with socket(AF_INET, SOCK_STREAM) as sock:
    #print(welcoming)
    print("Renseigner votre login : ")
    sock.connect((sys.argv[1], int(sys.argv[2])))
    
    while True :
        mess = input()
        sock.sendall(mess.encode())
        reponse = sock.recv(TAILLE_TAMPON)
        
        print(reponse.decode())
        
        if mess.lower() == "/quit":
            break
            
             FIX ME : break qui se declenche trop tot pour le serveur en cas de 'quit'
            
    
sys.exit(0) # En cas de sortie de la boucle, fin du client. Normalement implicite 

'''
   
# Définition d'un client réseau gérant en parallèle l'émission
# et la réception des messages (utilisation de 2 THREADS).

import socket, sys, threading

class ThreadReception(threading.Thread):
    """objet thread gérant la réception des messages"""
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn           # réf. du socket de connexion
   
    def run(self):
        #print(welcoming)
        print("Renseigner votre login : ")
        
        while 1:
            message_recu = self.connexion.recv(1024).decode()
            print ("*" + message_recu + "*")
            if message_recu.lower() == "/quit":
                break
            
            # Le thread <réception> se termine ici.
            # On force la fermeture du thread <émission> :
        th_E.Thread__stop()
        print ("Client arrêté. Connexion interrompue.")
        self.connexion.close()
            
class ThreadEmission(threading.Thread):
    """objet thread gérant l'émission des messages"""
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn           # réf. du socket de connexion
   
    def run(self):
        while 1:
            message_emis = input()
            self.connexion.send(message_emis.encode())
            
            
# Programme principal - Établissement de la connexion :
connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = sys.argv[1]
port = int(sys.argv[2])

try:
    connexion.connect((host, port))
except socket.error:
    print ("La connexion a échoué.")
    sys.exit()    

print ("Connexion établie avec le serveur.")
            
# Dialogue avec le serveur : on lance deux threads pour gérer
# indépendamment l'émission et la réception des messages :
th_E = ThreadEmission(connexion)
th_R = ThreadReception(connexion)
th_E.start()
th_R.start()                 