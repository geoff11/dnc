from setuptools import command

__author__ = 'think'
import sys
import threading
from socket import *
from tkinter import *
from time import *
import select

class DNCservGUI(object) :
    def __init__(self,host="local host",port=8000):
        self.top = Tk ()
        self.top.title ("Dog is Not a Chat server")

        #creer le socket
        self.ChatSerSock =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.ChatSerSock.bind((host,port))
        self.ChatSerSock.listen(8)


        #reserver le menu de la fonction
        self.menubar = Menu(self.top)
        for item in ["SLEEP","LIST","QUIT","WAKE","LOGCHANGE","PRIVATE","ACCEPTPC","DENYPC","STOPPC","FILESEND","FILEACC","FILEDEN"] :
            self.menubar.add_command(label = "About" , command = self.OnAbout)
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
        self.sendMesgButton = Button(self.frame[1],text='Send',width=10,command=self.OnsendMessage)
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
         # this has no effect, why ?
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(("0.0.0.0", PORT))
        server_socket.listen(10)

        # Add server socket to the list of readable connections
        CONNECTION_LIST.append(server_socket)

        print ("Chat server started on port " + str(PORT))









    #envoyer les messages
    def OnSendMessage(self):
        self.send_data=''
        self.send_data=self.MessageIn.get()
        if self.send_data:
            self.MessageOut.insert(END,'you said [%s]:'% ctime())
            self.MessageOut.insert(END,self.send_data)
            self.MessageOut.insert(END,'')
            self.MessageIn.delete(0,self.send_data.__len__())
            self.ChatClitSock.send(self.send_data)
        elif :
            cmd == "SLEEP"
            reponce
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
    def mutiThread(self):
        threading.Thread.start_new_thread(self.SocketProc_recv,())

def main():
    pp=DNCservGUI()
    pp.mutiThread()
    mainloop()

if __name__=='__main__':
    main()
    #s




