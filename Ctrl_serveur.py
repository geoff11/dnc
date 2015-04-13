import os,sys,threading
from socket import *

# Jaune 1 Team -- DNC Server  

# -*- coding: utf-8 -*- 
from socket import *
from datetime import *
import Chat

#conn_client = {} # TODO : mettre dans chat

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
        #conn_client[userActif] = self.conn # une connexion par user
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
        #del conn_client[userActif]        # supprimer son entrée dans le dictionnaire
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
        pseudoDest = ""
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
                    reponseClient = "Please specify your new pseudo"
                    
            elif cmd ==  "private":
                if len(message) > 1:
                    pseudoDest = message[1]
                    reponseSpecifyClient = self.chat.private(userActif.getPseudo, pseudoDest)
                    if reponseSpecifyClient == "":
                        reponseClient = pseudoDest + " is not present in the chat"
                    else:
                        reponseClient = userActif.private(pseudoDest)
                else :
                    reponseClient = "Please specify a pseudo"
                
            elif cmd == "acceptpc":
                reponseClient = userActif.acceptpc()
                
            elif cmd == "denypc":
                reponseClient = userActif.denypc()
                
            elif cmd == "stoppc":
                reponseClient = userActif.stoppc()
                
            elif cmd == "filesend":
                reponseClient = userActif.filesend()
                
            elif cmd == "fileacc":
                reponseClient = userActif.fileacc()
                
            elif cmd == "fileden":
                reponseClient = userActif.fileden()
                
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
            self.sendToAClient(userActif.getPseudo(), pseudoDest, reponseSpecifyClient)
                
    
    def sendToAll(self, userActif, message):
        '''
            Envoi du message a tous les users actifs excepte l'emetteur
        '''
        
        for u in self.chat.listeClients:
            if userActif != u and u.getNumState() == 1 and userActif.getNumState() == 1 :
                u.getConn().send(userActif.getPseudo().encode() + ": ".encode() + message.encode())
    
    def sendToAClient(self, pseudoEm, pseudoDest, msg):
        
        for u in self.chat.listeClients:
            if pseudoDest == u.getPseudo() :
                u.getConn().send(pseudoDest.encode() + ": ".encode() + msg.encode())
                # faire une boucle pour la reponse / gerer thread
                

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

