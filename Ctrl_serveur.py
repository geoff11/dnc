import os,sys,threading
from socket import *

# Jaune 1 Team -- DNC Server  

# -*- coding: utf-8 -*- 
from socket import *
from datetime import *
import Chat


class Ctrl_serveur(threading.Thread):
    
    '''
    Classe Ctrl_serveur
    '''
    
    def __init__(self, port, sock):
        '''
            
        '''
        self.port = port
        self.chat = Chat.Chat() # création du chat
        self.maSock = sock
        threading.Thread.__init__(self)
        
    def run(self):
        print('Waiting for connections on port %s' % (self.port))
        
        # Nouvelle connexion= nouveau thread
        
        while True:
            conn, addr = self.maSock.accept()
            threading.Thread(target=self.manageCommands, args=(conn, addr)).start()
        
        conn.close() # fermeture du thread
            
                
    def identifyClient(self, conn):
        # Recuperation de la requete du client
        pseudo = conn.recv(TAILLE_TAMPON)
        logDispo = self.chat.verifLogin(pseudo)
        
        
        if logDispo:
            repLogOK = "Login successful !! Let's get started"
            conn.sendall(repLogOK.encode())
            return self.chat.addClient(pseudo, conn)

                
        while (not logDispo):
            # Envoi de la reponse negative de log au client
            repLog = "Log already used ! Please choose another one"
            conn.send(repLog.encode())
            # Recuperation du Nieme essai
            pseudo = conn.recv(TAILLE_TAMPON)
            logDispo = self.chat.verifLogin(pseudo)
            
            if logDispo:
                repLogOK = "Login successful !! Let's get started"
                conn.sendall(repLogOK.encode())
                return self.chat.addClient(pseudo, conn)
    


    def manageCommands(self, conn, addr):
        
        print('Client connected with ' + addr[0] + ':' + str(addr[1]))
        userActif = self.identifyClient(conn)
        self.sendToAll(userActif, "is online")
        
        while True:
            try:
                # Recuperation de la commande
                recu = conn.recv(TAILLE_TAMPON)
                message = recu.decode().lower().split() # on découpe le message en tableau de mots
                
                
                #Gestion du cas ou le client ne tape rien
                if len(message) > 0:
                    cmd = message[0]
                else:
                    error = "Error : please type something"
                    userActif.getThread().sendall(error.encode())
                    
                reponseAll = ""
                
                # Construction de la reponseClient
                
                reponseClient = ""
                
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
                    reponseClient = ""    # Si la reponse concerne tout le monde, elle ne concerne pas le client seul CQF
                    reponseAll = cmd
                
                
                # dabord rep a tlm en cas de deconnexion
                if reponseAll != "" :
                    self.sendToAll(userActif, reponseAll)
                    
                # Envoi de la reponseClient au client
                # !! Si une reponse doit etre envoyee a un seul client
                if reponseClient != "":
                    userActif.getThread().sendall(reponseClient.encode())
                
                
                
            except KeyboardInterrupt: break
        
        self.chat.deleteClient(userActif)
    
    
    def sendToAll(self, userActif, message):
        '''
            Envoi du message a tout le monde
        '''
        for u in self.chat.listeClients:
            if u != userActif:
                u.getThread().sendall(userActif.getPseudo() + ": ".encode() + message.encode())
        
        

if __name__ == '__main__':
  
    if len(sys.argv) != 2 :
        print("Usage: {} <port>".format(sys.argv[0]))
        sys.exit(1)
    
    TAILLE_TAMPON = 256
    
    # Ouverture en ecriture du fichier de log
    logs = open("serveur.log", "w")
        
    maSock = socket(AF_INET, SOCK_STREAM)
    try:
        maSock.bind(('', int(sys.argv[1])))
    except socket.error:
        print('Bind failed %s' % (socket.error))
        sys.exit()
            
    maSock.listen(100) # 100 clients peuvent se connecter en meme temps maxi
    print("Serveur en attente sur le port {} .".format(sys.argv[1],), file=logs)  # Ecriture du fichier de log  
        
    server = Ctrl_serveur(sys.argv[0], maSock)
    server.run()
        
    maSock.close()
    print("Arret du serveur", file=logs)
    logs.close() 
    sys.exit(0)


