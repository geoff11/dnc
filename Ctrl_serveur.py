import os,sys,threading
from socket import *

# Jaune 1 Team -- DNC Server  

# -*- coding: utf-8 -*- 
from socket import *
from datetime import *
import Chat

conn_client = {} # TODO : mettre dans chat

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
        conn_client[userActif] = self.conn # une connexion par user
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
        del conn_client[userActif]        # supprimer son entrée dans le dictionnaire
        self.chat.deleteClient(userActif)
        print ("Client %s logs out" % userActif)
        # Le thread se termine ici
            
                
    def identifyClient(self):
        # Recuperation de la requete du client
        pseudo = self.conn.recv(TAILLE_TAMPON)
        logDispo = self.chat.verifLogin(pseudo)
        
        
        if logDispo:
            repLogOK = "Login successful !! Let's get started"
            self.conn.send(repLogOK.encode())
            return self.chat.addClient(pseudo)

                
        while (not logDispo):
            # Envoi de la reponse negative de log au client
            repLog = "Log already used ! Please choose another one"
            self.conn.send(repLog.encode())
            # Recuperation du Nieme essai
            pseudo = self.conn.recv(TAILLE_TAMPON)
            logDispo = self.chat.verifLogin(pseudo)
            
            if logDispo:
                repLogOK = "Login successful !! Let's get started"
                self.conn.send(repLogOK.encode())
                return self.chat.addClient(pseudo)
    


    def manageCommands(self, userActif, message):
                
        reponseAll = "" # Construction de la reponse pour tous les clients
        reponseClient = "" # Construction de la reponseClient        
        
        mess = message[0]
                    
        if len(mess) > 0 and str(mess[0]) == "/" :
            
            cmd = str(mess[1:])
            
            if cmd == "sleep":
                reponseClient = userActif.sleep()
            elif cmd == "list":
                reponseClient = self.chat.list()
            elif cmd == "quit":
                reponseClient = userActif.quit()
                if len(message) > 1:
                    reponseAll = self.chat.quit(userActif, message[1])
                else:
                    reponseAll = self.chat.quit(userActif)
            elif cmd == "wake":
                reponseClient = userActif.wake()
            elif cmd == "logchange":
                reponseClient = userActif.logchange()
            elif cmd ==  "private":
                reponseClient = userActif.private()
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
                
    
    def sendToAll(self, userActif, message):
        '''
            Envoi du message a tous les users actifs excepte l'emetteur
        '''
        
        for u in conn_client:
            if userActif != u and u.getNumState() == 1 :
                conn_client[u].send(userActif.getPseudo() + ": ".encode() + message.encode())
        
        

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
    
    ################
    
    print('Waiting for connections on port %s' % (int(sys.argv[1])))
    
    # Attente et prise en charge des connexions demandées par les clients :
    conn_client = {}                # dictionnaire des connexions clients
    chat = Chat.Chat() # création du chat
    
    while True :    
        connexion, adresse = maSock.accept()
        # Créer un nouvel objet thread pour gérer la connexion :
        th = Thread_client(adresse, connexion, chat)
        th.start()
         
        print ("Nouveau client : adresse IP %s, port %s." %\
            (adresse[0], adresse[1]))
    
    
    sys.exit(0)

