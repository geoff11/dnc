import os,sys,threading
from socket import *

# Jaune 1 Team -- DNC Server  

# -*- coding: utf-8 -*- 
from socket import *
from datetime import *
from modele import Chat


class Thread_client(threading.Thread):
    
    '''
    Classe Thread_client
    '''
    
    def __init__(self, pAdr, pConn, pChat):
        '''
            
        '''
        self.adr = pAdr
        self.chat = pChat
        self.conn = pConn
        threading.Thread.__init__(self)
        
    def run(self):
        
        conn = self.conn
        addr = self.adr
        
        print('Client connected with ' + addr[0] + ':' + str(addr[1]))
        userActif = self.identifyClient()
        self.sendToAll(userActif, "is online")
        
        while True:
            try:
                # Recuperation de la commande
                recu = conn.recv(TAILLE_TAMPON)
                message = recu.decode().lower().split() # on découpe le message en tableau de mots
                
                # Gestion du cas ou le client ne tape rien
                if len(message) > 0:
                    self.manageCommands(userActif, message)
                    
                    if message[0] == "/quit":
                        conn.send("/quit".encode())
                        break;
                    
                else:
                    error = "Error : please type something"
                    conn.send(error.encode())
            
            except KeyboardInterrupt: break
        
        
        # Fermeture de la connexion :
        self.conn.close()      # couper la connexion côté serveur
        print ("Client %s logs out" % userActif.getPseudo())
        self.chat.deleteClient(userActif)
        # Le thread se termine ici
            
                
    def identifyClient(self):
        # Recuperation de la requete du client
        pseudo = self.conn.recv(TAILLE_TAMPON).decode()
        logDispo = self.chat.verifLogin(pseudo)
        
        
        if logDispo:
            repLogOK = "Login successful !! Let's get started"
            self.conn.send(repLogOK.encode())
            return self.chat.addClient(pseudo, self.conn)

                
        while (not logDispo):
            # Envoi de la reponse negative de log au client
            repLog = "Log already used ! Please choose another one"
            self.conn.send(repLog.encode())
            # Recuperation du Nieme essai
            pseudo = self.conn.recv(TAILLE_TAMPON).decode()
            logDispo = self.chat.verifLogin(pseudo)
            
            if logDispo:
                repLogOK = "Login successful !! Let's get started"
                self.conn.send(repLogOK.encode())
                return self.chat.addClient(pseudo, self.conn)
    


    def manageCommands(self, userActif, message):
                
        reponseAll = "" # Construction de la reponse pour tous les clients
        reponseClient = "" # Construction de la reponse au client actif   
        reponseSpecifyClient = "" # Construction de la reponse d un client specifique : mp 
        otherPseudo = ""
        myPseudo = userActif.getPseudo()
        mess = message[0]
                    
        if len(mess) > 0 and str(mess[0]) == "/" :
            
            cmd = str(mess[1:]) 
            
            if cmd == "sleep":
                if len(message) > 1:
                    reponseAll = self.chat.sleep(userActif, message[1])
                else:
                    reponseAll = self.chat.sleep(userActif)
                reponseClient = userActif.sleep()
                
            elif cmd == "list":
                reponseClient = self.chat.list()
                
            elif cmd == "quit":
                if len(message) > 1:
                    reponseAll = self.chat.quit(userActif, message[1])
                else:
                    reponseAll = self.chat.quit(userActif)
                reponseClient = userActif.quit()
                
            elif cmd == "wake":
                if len(message) > 1:
                    reponseAll = self.chat.wake(userActif, message[1])
                else:
                    reponseAll = self.chat.wake(userActif)
                reponseClient = userActif.wake()
                
            elif cmd == "logchange":
                if len(message) > 1:
                    newPseudo = message[1]
                    reponseAll = self.chat.logchange(userActif, newPseudo)
                    if reponseAll != "" :
                        reponseClient = userActif.logchange(newPseudo)
                    else:
                        reponseClient = "Pseudo already used, please choose another one"
                else :
                    reponseClient = "Usage : /logchange <newpseudo>"
                    
            elif cmd ==  "private":
                if len(message) == 2:
                    otherPseudo = message[1] # destinataire
                    userDest = self.chat.getClientByPseudo(otherPseudo)
                    
                    if userDest :
                        reponseClient = userActif.private(userDest)
                    
                        if reponseClient == "" : # bien passe
                            
                            reponseSpecifyClient = self.chat.private(myPseudo, otherPseudo)
                            
                            if reponseSpecifyClient == "":
                                reponseClient = otherPseudo + " is not present in the chat"
                            else:
                                reponseClient = "Your request has been sent to " + otherPseudo
                            
                else :
                    reponseClient = "Usage : /private <pseudo>"
                   
            elif cmd == "acceptpc":
                 if len(message) == 2:
                    otherPseudo = message[1] # emetteur
                    userEm = self.chat.getClientByPseudo(otherPseudo)
                    reponseClient = userActif.acceptpc(userEm)
                    
                    if reponseClient != "" :
                        reponseSpecifyClient = "Private connexion opened between " + myPseudo + " and you"
                 else :
                    reponseClient = "Usage : /acceptpc <pseudo>"
                
            elif cmd == "denypc":
                if len(message) == 2:
                    otherPseudo = message[1] # emetteur
                    userEm = self.chat.getClientByPseudo(otherPseudo)
                    reponseClient = userActif.denypc(userEm)
                    
                    if reponseClient != "" :
                        reponseSpecifyClient = "Private connexion was denied by " + myPseudo
                        
                else :
                    reponseClient = "Usage : /denypc <pseudo>"
                
            elif cmd == "stoppc":
                
                if len(message) == 2:
                    otherPseudo = message[1] # peut etre l emetteur ou le recepteur d origine
                    user2 = self.chat.getClientByPseudo(otherPseudo)
                    reponseClient = userActif.stoppc(user2)
                    
                    if reponseClient != "" :
                        reponseSpecifyClient = "Private connexion was closed by " + myPseudo
                    
                else :
                    reponseClient = "Usage : /stoppc <pseudo>"
            
            elif cmd == "mp":
                if len(message) == 3:
                    otherPseudo = message[1] # peut etre l emetteur ou le recepteur d origine
                    user2 = self.chat.getClientByPseudo(otherPseudo)
                    reponseClient = userActif.mp(user2)
                    
                    if reponseClient != "":
                        reponseSpecifyClient = "MP => " + message[2]
                else :
                    reponseClient = "Usage : /mp <pseudo> <msg>"
                    
                    
            elif cmd == "filesend":
                reponseClient = userActif.filesend()
                
            elif cmd == "fileacc":
                reponseClient = userActif.fileacc()
                
            elif cmd == "fileden":
                reponseClient = userActif.fileden()
            else :
                reponseClient = "With '/' you can use : sleep, list, quit, wake, logchange, private, acceptpc, denypc, mp, stoppc, filesend, fileacc, fileden"
                
        else :
            reponseAll = mess
        
        
        # d'abord rep a tlm en cas de deconnexion
        if reponseAll != "" :
            self.sendToAll(userActif, reponseAll)
            
        # Envoi de la reponseClient au client
        # !! Si une reponse doit etre envoyee a un seul client
        if reponseClient != "":
            self.conn.send(reponseClient.encode())
        
        if reponseSpecifyClient != "":
            self.sendToAClient(myPseudo, otherPseudo, reponseSpecifyClient)
                
    
    def sendToAll(self, userActif, message):
        '''
            Envoi du message a tous les users actifs excepte l'emetteur
        '''
        myPseudo = userActif.getPseudo()
        
        for u in self.chat.listeClients:
            if userActif != u and u.getNumState() == 1 and userActif.getNumState() == 1 :
                u.getConn().send(myPseudo.encode() + ": ".encode() + message.encode())
    
    def sendToAClient(self, pseudoEm, otherPseudo, msg):
        
        for u in self.chat.listeClients:
            if otherPseudo == u.getPseudo() :
                u.getConn().send(pseudoEm.encode() + ": ".encode() + msg.encode())
    
                

if __name__ == '__main__':
  
    if len(sys.argv) != 2 :
        print("Usage: {} <port>".format(sys.argv[0]))
        sys.exit(1)
    
    TAILLE_TAMPON = 1024
    
    # Ouverture en ecriture du fichier de log
    logs = open("serveur.log", "w")
        
    maSock = socket(AF_INET, SOCK_STREAM)
    
    try:
        maSock.bind(('', int(sys.argv[1])))
    except socket.error:
        print('Bind failed %s' % (socket.error))
        sys.exit()
    
    maSock.listen(4)
    
    print('Waiting for connections on port %s' % (int(sys.argv[1])))
    chat = Chat.Chat() # création du chat
    
    while True :    
        connexion, adresse = maSock.accept()
        # Créer un nouvel objet thread pour gérer la connexion :
        th = Thread_client(adresse, connexion, chat)
        th.start()    
    
    sys.exit(0)

