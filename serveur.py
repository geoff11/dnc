from setuptools import command

__author__ = 'think'
import sys.os.os.path
from socket import *
import _thread
from Tkinter import *
from time import *

class DNC(object) :
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





