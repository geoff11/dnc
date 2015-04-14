from _socket import SOCK_DGRAM
from concurrent.futures import thread
from setuptools import command

__author__ = 'Liwen'
import sys
import threading
import socket
from tkinter import *
from time import ctime
import select

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

        '''CONNECTION_LIST = []
        RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
        PORT = 5000

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(("0.0.0.0", PORT))
        server_socket.listen(10)

        # Add server socket to the list of readable connections
        CONNECTION_LIST.append(server_socket)

        print ("Chat server started on port " + str(PORT))'''

    def manageCommands(self, TAILLE_TAMPON, logs):
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


    #envoyer les messages
    def OnSendMessage(self, message=None):
        self.send_data=''
        self.send_data=self.MessageIn.get()
        if self.send_data:
            self.MessageOut.insert(END,'you said [%s]:'% ctime())
            self.MessageOut.insert(END,self.send_data)
            self.MessageOut.insert(END,'')
            self.MessageIn.delete(0,self.send_data.__len__())
            self.ChatClitSock.send(self.send_data)



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
    def OnQuit(self):
        self.ChatSerSock.close()
        self.top.quit()


    #About
    def OnAbout(self):
        pass

    #mult
    #def mutiThread(self):
    #    threading.start_new_thread(self.SocketProc_recv,())

def main():
    pp=DNCservGUI()
    #pp.mutiThread()
    mainloop()

if __name__=='__main__':
    main()
   # if len(sys.argv) != 2 :
   #     print("Usage: {} <port>".format(sys.argv[0]))
    #    sys.exit(1)

   # TAILLE_TAMPON = 256

    # Ouverture en ecriture du fichier de log
   # logs = open("serveur.log", "w")

   # maSock = socket(AF_INET,SOCK_DGRAM)
   # maSock.bind(('',int(sys.argv[1])))
   # print("Serveur en attente sur le port {} .".format(sys.argv[1],), file=logs)  # Ecriture du fichier de log

   # ctrl = serveur(maSock)
   # ctrl.manageCommands()

   # maSock.close()
   # print("Arret du serveur", file=logs)
   # logs.close()
   # sys.exit(0)




