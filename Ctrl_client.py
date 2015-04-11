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
        sock.send(mess.encode())
        reponse = sock.recv(TAILLE_TAMPON)
        
        print(reponse.decode())
        
        if mess.lower() == "quit":
            break
            ''' FIX ME : break qui se declenche trop tot pour le serveur en cas de 'quit'
            '''
    
    sock.close()
    
sys.exit(0) # En cas de sortie de la boucle, fin du client. Normalement implicite 