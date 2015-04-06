__author__ = 'think'
from time import ctime
from tkinter import *
import socket
import threading
import sys

class DNCclitGUI(object):
    def __init__(self):
        self.top=Tk()
        self.top.title('Dog is Not a Chat client')

        #creer le socket
        self.ChatClitSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.ChatClitSock.connect(('localhost',8000))

        #reserver le menu de fonction
        self.menubar=Menu(self.top)
        for item in ["SLEEP","LIST","QUIT","WAKE","LOGCHANGE","PRIVATE","ACCEPTPC","DENYPC","STOPPC","FILESEND","FILEACC","FILEDEN"]:
            self.menubar.add_command(label=item)
        self.menubar.add_command(label='About',command=self.OnAbout)
        self.top['menu']=self.menubar

        #Creer le Frame
        self.frame=[]
        self.frame.append(Frame())
        self.frame.append(Frame())


        # Barre de defilement de zone de liste de sortie de message
        self.slbar=Scrollbar(self.frame[0])
        self.slbar.pack(side=RIGHT,fill=Y)

         #creer la boite de sortie de message, et puis lier le barre de defilement
        self.MessageOut=Listbox(self.frame[0],height=25,fg='red')
        self.MessageOut['yscrollcommand']=self.slbar.set
        self.MessageOut.pack(expand=1,fill=BOTH)
        self.slbar['command']=self.MessageOut.yview
        self.frame[0].pack(expand=1,fill=BOTH)


         #creer ENTRY pour l'entree de message
        self.MessageIn=Entry(self.frame[1],width=60,fg='red')
        self.MessageIn.pack(fill=X,expand=1,pady=10,padx=15)

        #creer le buttn pour envoyer le truc
        self.sendMesgButton=Button(self.frame[1],
                                   text='Send',
                                   width=10,
                                   command=self.OnSendMessage)
        #self.sendMesgButton.bind("<Return>",self.SendMessageTo)
        self.sendMesgButton.pack(side=BOTTOM and RIGHT,padx=20,pady=10)

        #creer le button pour quitter
        self.quitButton=Button(self.frame[1],text='Quit',width=10,command=self.OnQuit)
        self.quitButton.pack(side=RIGHT,padx=20,pady=10)
        self.frame[1].pack()


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
        else:
            pass

    def SocketProc_recv(self):
        self.buffer=1024
        self.recv_data=''
        while True:
            try:
                self.recv_data=self.ChatClitSock.recv(self.buffer)
            except socket.error as e:
                break
            self.MessageOut.insert(END,'Your friend said  [%s]:' % ctime())
            self.MessageOut.insert(END,self.recv_data)
            self.MessageOut.insert(END,'')

    #quit
    def OnQuit(self):
        self.top.quit()
        self.ChatClitSock.close()


    #About
    def OnAbout(self):
        pass

    #mult
    def mutiThread(self):
        threading.Thread.start_new_thread(self.SocketProc_recv,())

def main():
    pp=DNCclitGUI()
    pp.mutiThread()
    mainloop()

if __name__=='__main__':
    main()
    #ddddddd
