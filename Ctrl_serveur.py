import os,sys
from socket import *

# Jaune 1 Team -- DNC Server  

# -*- coding: utf-8 -*- 
from socket import *
from datetime import *
import Chat


class Ctrl_serveur:
    
    '''
    Classe Ctrl_serveur
    '''
    
    def __init__(self, sock):
        '''
            Initialisation du user
        '''
        self.chat = Chat.Chat() # création du chat
        self.maSock = sock


    def manageCommands(self):
        while True:
            try:
                # Recuperation de la requete du client
                requete = self.maSock.recvfrom(TAILLE_TAMPON)
                
                # Extraction du message, de l adresse et du pseudo sur le client
                (mess, adr_client) = requete
                ip_client, port_client = adr_client
                user = self.chat.identifierClient(ip_client, port_client, mess)
                # FIXME : Le passage systematique dans identifierClient induit des problemes comportementaux
                # TODO : Modulariser le Login par une fonction, 
                # le chat fait que de la merde en passant toujours par le login xD
                
                while (user == 0):
                    # Envoi de la reponse negative de log au client
                    repLog = "Log already used ! Please choose another one"
                    self.maSock.sendto(repLog.encode(), adr_client)
                    # Recuperation du 2eme essai
                    requete = self.maSock.recvfrom(TAILLE_TAMPON)
                    # Extraction du message, de l adresse et du pseudo sur le client
                    (mess, adr_client) = requete
                    ip_client, port_client = adr_client
                    user = self.chat.identifierClient(ip_client, port_client, mess)
                    
                if user != 0:
                    repLogOK = "Login successful !!"
                    self.maSock.sendto(repLogOK.encode(), adr_client)
                # SOME SHIT : Cet envoi doit se faire une seule fois 
            
                message = mess.decode().lower().split() # on découpe le message en tableau de mots
                #Gestion du cas ou le client ne tape rien
                if len(message)>0:
                    cmd = message[0]
                else:
                    error = "Error : please type something"
                    self.maSock.sendto(error.encode(), adr_client)
                reponseAll = ""
                
                
                print("Requete provenant de {}. Longueur = {}". \
                format(ip_client, len(mess)), file=logs)      # Ecriture du fichier de log   
                
                # Construction de la reponseClient
                
                if cmd == "sleep":
                    reponseClient = user.sleep()
                elif cmd == "list":
                    reponseClient = self.chat.list()
                elif cmd == "quit":
                    reponseClient = user.quit()
                    if len(message) > 1:
                        reponseAll = self.chat.quit(user.getPseudo(),message[1])
                    else:
                        reponseAll = self.chat.quit(user.getPseudo())
                elif cmd == "wake":
                    reponseClient = user.wake()
                elif cmd == "logchange":
                    reponseClient = user.logchange()
                elif cmd ==  "private":
                    reponseClient = user.private()
                elif cmd == "acceptpc":
                    reponseClient = user.acceptpc()
                elif cmd == "denypc":
                    reponseClient = user.denypc()
                elif cmd == "stoppc":
                    reponseClient = user.stoppc()
                elif cmd == "filesend":
                    reponseClient = user.filesend()
                elif cmd == "fileacc":
                    reponseClient = user.fileacc()
                elif cmd == "fileden":
                    reponseClient = user.fileden()
                else :
                    reponseClient=""    # Si la reponse concerne tout le monde, elle ne concerne pas le client seul CQF
                    self.sendToAll(mess)
                
                # Envoi de la reponseClient au client
                # !! Si une reponse doit etre envoyee a un seul client
                if reponseClient != "":
                    self.maSock.sendto(reponseClient.encode(), adr_client)
                
                if reponseAll != "" :
                    self.sendToAll(reponseAll.encode())
                
            except KeyboardInterrupt: break
        
    
    
    
    def sendToAll(self, message):
        '''
            Envoi du message a tout le monde
        '''
        for item in self.chat.listeClients:
            self.maSock.sendto(message, item.getAdr())
            
        
        
        

if __name__ == '__main__':
  
    if len(sys.argv) != 2 :
        print("Usage: {} <port>".format(sys.argv[0]))
        sys.exit(1)
    
    TAILLE_TAMPON = 256
    
    # Ouverture en ecriture du fichier de log
    logs = open("serveur.log", "w")
        
    maSock = socket(AF_INET,SOCK_DGRAM)
    maSock.bind(('',int(sys.argv[1])))
    print("Serveur en attente sur le port {} .".format(sys.argv[1],), file=logs)  # Ecriture du fichier de log  
        
    ctrl = Ctrl_serveur(maSock)
    ctrl.manageCommands()   
        
    maSock.close()
    print("Arret du serveur", file=logs)
    logs.close() 
    sys.exit(0)


