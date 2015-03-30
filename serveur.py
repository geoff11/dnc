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

