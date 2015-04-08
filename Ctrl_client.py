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


with socket(AF_INET, SOCK_DGRAM) as sock:
    print(welcoming)
    print("Renseigner votre login : ")
    
    while True :
        mess = input()
        sock.sendto(mess.encode(), (sys.argv[1], int(sys.argv[2])))
        reponse, _ = sock.recvfrom(TAILLE_TAMPON)
        
        print(reponse.decode())
        
        if mess.lower() == "quit": 
            break
    
sys.exit(0) # En cas de sortie de la boucle, fin du client. Normalement implicite 