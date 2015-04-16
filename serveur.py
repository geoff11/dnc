from _socket import SOCK_DGRAM
from concurrent.futures import thread
from setuptools import command

__author__ = 'yellow 2'
import sys
import threading
import socket
from tkinter import *
from time import ctime
import select

'''
Initialisation de la fenetre du chat
creation du pseudo utilisateur
'''
class DNCservGUI(object) :
    def __init__(self,host="localhost",port=2222):
        self.top = Tk ()
        self.top.title ("Dog is Not a Chat server")

        #creer le socket
        self.ChatSerSock =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.ChatSerSock.bind((host,port))
        self.ChatSerSock.listen(8)


        #reserver le menu de la fonction
        self.menubar = Menu(self.top)
        for item in ["SLEEP","LIST","QUIT","WAKE","LOGCHANGE","PRIVATE","ACCEPTPC","DENYPC","STOPPC","FILESEND","FILEACC","FILEDEN"] :
            self.menubar.add_command(label =item , command = self.OnAbout)
            self.top["menu"]= self.menubar

        #creer le Frame
        self.frame=[]
        self.frame.append(Frame())
        self.frame.append(Frame())

        # Barre de defilement de zone de liste de sortie de message
        self.slbar = Scrollbar(self.frame[0])
        self.slbar.pack(side=RIGHT , fill=Y)

        #creer la boite de sortie de message, et puis lier le barre de defilement
        self.MessageOut = Listbox(self.frame[0],height = 25, fg ='red')
        self.MessageOut['yscrollcommand']=self.slbar.set
        self.MessageOut.pack(expand=1,fill=BOTH)
        self.slbar['command']=self.MessageOut.yview
        self.frame[0].pack(expand=1,fill=BOTH)

        #creer ENTRY pour l'entree de message
        self.MessageIn = Entry (self.frame[1],width = 65, fg='red')
        self.MessageIn.pack(expand = 1, fill = X ,pady=10,padx=15)

        #creer le buttn pour envoyer le truc
        self.sendMesgButton = Button(self.frame[1],text='Send',width=10,command=self.OnSendMessage)
        #self.sendMesgButton.bind("<Return>",self.SendMessageTo)
        self.sendMesgButton.pack(side=BOTTOM and RIGHT , padx=20,pady=10)

        #creer le button pour quitter
        self.quitButton=Button(self.frame[1],text='Quit',width=10,command=self.OnQuit)
        self.quitButton.pack(side=RIGHT,padx=20,pady=10)
        self.frame[1].pack()

        CONNECTION_LIST = []
        RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
        PORT = 5000

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(("0.0.0.0", PORT))
        server_socket.listen(10)

        # Add server socket to the list of readable connections
        CONNECTION_LIST.append(server_socket)

        print ("Chat server started on port " + str(PORT))
        
    def Client(self,connexionDispo=None, RECV_BUFFER=None):

        pseudo = self.conn.recv(RECV_BUFFER).decode()
        
        pseudoDisponible = self.dnc.login(pseudo)
            
            
        if connexionDispo:
            
            OK = "vous etes connecté !!"
            self.conn.send(OK.encode())
            
            return self.dnc.addUser(pseudo, self.connexion)
    
                    
        while not pseudoDisponible:

            reponseLog = "deja utilisé !!"
            
            self.connexion.send(reponseLog.encode())

            pseudo = self.connexion.recv(RECV_BUFFER).decode()
            
            logDispo = self.dnc.login(pseudo)
                
            if logDispo:
                
                reponseOK = "Login successful !! Let's get started"
                self.conn.send(reponseOK.encode())
                
                return self.dnc.addUser(pseudo, self.connexion)

    



    def Commands(self, user, message, pseudoConnected=None):
        '''
            Methode : elle renvoie toute les fonctions du chat
        '''
        
        reponse = ""
        reponseNonActifs = ""
        reponseClient = "" 
        reponsePrivate = ""
        newPseudo = ""
        persoPseudo = pseudoConnected.getPseudo()
        msg = message[0]
                    
        if len(msg) > 0 and str(msg[0]) == "/" :
            
            messageParam = str(msg[1:]) 
    
            if messageParam == "sleep":
                
                if len(message) > 1:
                
                    reponseNonActifs = self.dnc.sleep(pseudoConnected, message[1])
                    
                else:
                    
                    reponseNonActifs = self.dnc.sleep(pseudoConnected)
                    
                reponseClient = pseudoConnected.sleep()
            
############################################################################################################
                
            elif messageParam == "list":
                
                reponseClient = self.dnc.listePseudo()

############################################################################################################
                
            elif messageParam == "wake":
                
                if len(message) > 1:
                    
                    reponseNonActifs = self.dnc.wake(pseudoConnected, message[1])
                    
                else:
                    
                    reponseNonActifs = self.dnc.wake(pseudoConnected)
                    
                reponseClient = pseudoConnected.wake()
                
############################################################################################################
                
            elif messageParam == "logchange":
                
                if len(message) > 1:
                    
                    pseudoUser = message[1]    
                    reponseNonActifs = self.dnc.logchange(pseudoConnected, newPseudo)
                    
                    if reponseNonActifs != "" :
                        
                        reponseClient = pseudoConnected.logchange(newPseudo)
                        
                    else:
                        
                        reponseClient = "Utiliser un autre pseudo"
                        
############################################################################################################
                    
            elif messageParam ==  "private":
                
                if len(message) == 2:
                    
                    newPseudo = message[1] # destinataire
                    userDest = self.dnc.getPseudoClient(newPseudo)
                    
                    if userDest :
                        
                        reponseClient = pseudoConnected.private(userDest)
                    
                        if reponseClient == "" : # bien passe
                            
                            reponsePrivate = self.dnc.private(persoPseudo, newPseudo)
                            
                            if reponsePrivate == "":
                                
                                reponseClient = newPseudo + " n'est pas connecté"
                                
                            else:
                                
                                reponseClient = "votre demande a été envoyé a : " + newPseudo
                            
############################################################################################################  
                 
            elif messageParam == "accept":
                
                 if len(message) == 2:
                     
                    newPseudo = message[1] # emetteur
                    emissionPrivate = self.dnc.getPseudoClient(newPseudo)
                    reponseClient = pseudoConnected.accept(emissionPrivate)
                    
                    if reponseClient != "" :
                        
                        reponsePrivate = "accepté par " + persoPseudo + ""
                        
############################################################################################################  
              
            elif messageParam == "deny":
                
                if len(message) == 2:
                    
                    newPseudo = message[1] # emetteur
                    emissionPrivate = self.dnc.getPseudoClient(newPseudo)
                    reponseClient = pseudoConnected.deny(emissionPrivate)
                    
                    if reponseClient != "" :
                        
                        reponsePrivate = "refusé par " + persoPseudo
                        
############################################################################################################      
          
            elif messageParam == "stop":
                
                if len(message) == 2:
                    
                    newPseudo = message[1]
                    user2 = self.dnc.getPseudoClient(newPseudo)
                    reponseClient = pseudoConnected.stop(user2)
                    
                    if reponseClient != "" :
                        
                        reponsePrivate = "fermé par" + persoPseudo
                    
 ############################################################################################################
            
            elif messageParam == "mp":
                
                if len(message) == 3:
                    
                    newPseudo = message[1] # peut etre l emetteur ou le recepteur d origine
                    user2 = self.dnc.getPseudoClient(newPseudo)
                    reponseClient = pseudoConnected.mp(user2)
                    
                    if reponseClient != "":
                        
                        reponsePrivate = "MP => " + message[2]
                        

############################################################################################################
                
    
    def sendUserActif(self, pseudoConnected, message):
        '''
            Envoi d'un message a tout les pseudo actifs dans le chat
        '''
        persoPseudo = pseudoConnected.getPseudo()
        
        for user in self.dnc.listeClients:
            
            if pseudoConnected != user and user.getNumEtat() == 1 and pseudoConnected.getNumEtat() == 1 :
                
                user.getConnexion().send("* ".encode() + persoPseudo.encode() + ":: ".encode() + message.encode() + " *".encode())
                
 ############################################################################################################   
 
 
    def sendAll(self, pseudoConnected, message):
        '''
            Envoi d'un message a tout les pseudo dans le chat
        '''
        persoPseudo = pseudoConnected.getPseudo()
        
        for user in self.dnc.listeClients:
            
            if user.getNumEtat() == 1 and pseudoConnected.getNumEtat() == 1 :
                
                user.getConnexion().send(persoPseudo.encode() + ":: ".encode() + message.encode())
                
############################################################################################################
    def sendPrivate(self, emission, newPseudo, msg, message=None):
        '''
            Envoi d'un message privé     
        '''
        
        for user in self.dnc.listePseudo:
            
            if newPseudo == user.getPseudo() :
                
                user.getConnexion().send("* ".encode() + emission.encode() + ":: ".encode() + message.encode() + " *".encode())


    #envoyer les messages
    def OnSendMessage(self, message=None, user=None,pseudoConnected=None,emission=None,newPseudo=None, msg=None):
        self.send_data=''
        self.send_data=self.MessageIn.get()
        self.send_data=self.MessageIn.Commands(self, user, message)
        self.send_data_all=self.MessageIn.sendAll(self, pseudoConnected, message)
        self.send_data_private=self.MessageIn.sendPrivate(self, emission, newPseudo, msg)

        if self.send_data:
            self.MessageOut.insert(END,'you said [%s]:'% ctime())
            self.MessageOut.insert(END,self.send_data)
            self.MessageOut.insert(END,'')
            self.MessageIn.delete(0,self.send_data.__len__())
            self.ChatClitSock.send(self.send_data)
        if self.sen_data_all:
            self.MessageOut.insert(END,'you said [%s]:'% ctime())
            self.MessageOut.insert(END,self.send_data_all)
            self.MessageOut.insert(END,'')
            self.MessageIn.delete(0,self.send_data.__len__())
            self.ChatClitSock.send(self.send_data)
        if self.send_data_private:
            self.MessageOut.insert(END,'you said [%s]:'% ctime())
            self.MessageOut.insert(END,self.send_data_private)
            self.MessageOut.insert(END,'')
            self.MessageIn.delete(0,self.send_data.__len__())
            self.ChatClitSock.send(self.send_data)
        #elif:
        #    messageParam == "sleep"
        #    reponce


         # Envoi du message a tout le monde
        for u in self.chat.listeClients:
           self.maSock.sendto(u.getPseudo() + ": ".encode() + message, u.getAdr())
    #socket communication
    def SocketProc_recv(self):
        self.buffer=1024
        self.MessageOut.insert(END,'Waiting for connection...')
        while True:
            self.ChatClitSock,self.clit_addr=self.ChatSerSock.accept()
            self.MessageOut.insert(END,'....connected already....')
            while True:
                self.recv_data=self.ChatClitSock.recv(self.buffer)
                if not self.recv_data:
                    break
                self.MessageOut.insert(END,'Your friend said  [%s]:' % ctime())
                self.MessageOut.insert(END,self.recv_data)
                self.MessageOut.insert(END,'')
            self.ChatSerSock.close()
            self.ChatClitSock.close()

    #quit
    def OnQuit(self, pseudoConnected=None):
        self.ChatSerSock.close()
        self.top.quit()
        self.dnc.deleteClient(pseudoConnected)

    #About
    def OnAbout(self):
        pass

    #mult
    def mutiThread(self):
        threading.start_new_thread(self.SocketProc_recv,())

def main():
    pp=DNCservGUI()
    #pp.mutiThread()
    mainloop()

if __name__=='__main__':
    main()
