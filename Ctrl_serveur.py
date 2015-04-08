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
            
        '''
        self.chat = Chat.Chat() # création du chat
        self.maSock = sock
        self.userActif = ""
        
    
    def identifyClient(self):
        # Recuperation de la requete du client
        log = self.maSock.recvfrom(TAILLE_TAMPON)
        # Extraction du pseudo, de l adresse  sur le client
        (pseudo, adr_client) = log
        ip_client, port_client = adr_client
        logDispo = self.chat.verifLogin(ip_client, port_client, pseudo)
        
        
        if logDispo:
            client = self.chat.addClient(ip_client, port_client, pseudo)
            repLogOK = "Login successful !! Let's get started"
            self.maSock.sendto(repLogOK.encode(), adr_client)
            self.userActif = client

                
        while (not logDispo):
            # Envoi de la reponse negative de log au client
            repLog = "Log already used ! Please choose another one"
            self.maSock.sendto(repLog.encode(), adr_client)
            # Recuperation du Nieme essai
            log = self.maSock.recvfrom(TAILLE_TAMPON)
            # Extraction du message, de l adresse sur le client
            (pseudo, adr_client) = log
            ip_client, port_client = adr_client
            logDispo = self.chat.verifLogin(ip_client, port_client, pseudo)
            
            if logDispo:
                client = self.chat.addClient(ip_client, port_client, pseudo)
                repLogOK = "Login successful !! Let's get started"
                self.maSock.sendto(repLogOK.encode(), adr_client)
                self.userActif = client
    


    def manageCommands(self):
        while True:
            try:
                # Recuperation de la commande
                requete = self.maSock.recvfrom(TAILLE_TAMPON)
                # Extraction du message, de l adresse et du pseudo sur le client
                (mess, adr_client) = requete
                ip_client, port_client = adr_client
                
                message = mess.decode().lower().split() # on découpe le message en tableau de mots
                
                
                #Gestion du cas ou le client ne tape rien
                if len(message) > 0:
                    cmd = message[0]
                else:
                    error = "Error : please type something"
                    self.maSock.sendto(error.encode(), adr_client)
                    
                reponseAll = ""
                
                
                print("Requete provenant de {}. Longueur = {}". \
                format(ip_client, len(mess)), file=logs)      # Ecriture du fichier de log   
                
                # Construction de la reponseClient
                
                reponseClient = ""
                
                if cmd == "serveurcrypteauthentificationclient1234569876newclient":
                    self.identifyClient()
                elif cmd == "sleep":
                    reponseClient = self.userActif.sleep()
                elif cmd == "list":
                    reponseClient = self.chat.list()
                elif cmd == "quit":
                    reponseClient = self.userActif.quit()
                    if len(message) > 1:
                        reponseAll = self.chat.quit(self.userActif,message[1])
                    else:
                        reponseAll = self.chat.quit(self.userActif)
                elif cmd == "wake":
                    reponseClient = self.userActif.wake()
                elif cmd == "logchange":
                    reponseClient = self.userActif.logchange()
                elif cmd ==  "private":
                    reponseClient = self.userActif.private()
                elif cmd == "acceptpc":
                    reponseClient = self.userActif.acceptpc()
                elif cmd == "denypc":
                    reponseClient = self.userActif.denypc()
                elif cmd == "stoppc":
                    reponseClient = self.userActif.stoppc()
                elif cmd == "filesend":
                    reponseClient = self.userActif.filesend()
                elif cmd == "fileacc":
                    reponseClient = self.userActif.fileacc()
                elif cmd == "fileden":
                    reponseClient = self.userActif.fileden()
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
        for u in self.chat.listeClients:
            self.maSock.sendto(u.getPseudo() + ": ".encode() + message, u.getAdr())
        
        

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


