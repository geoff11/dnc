__author__ = 'Liwen'
from time import ctime
from tkinter import *
import socket
import threading



class DNCclitGUI(object):
    """controle de client et la gestion de la fonction de client
        interface graphe de client
    """
    def __init__(self):
        self.top=Tk()
        self.top.title('Dog is Not a Chat client')

        #creer le socket
        self.ChatClitSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.ChatClitSock.connect(('localhost',2222))

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

    #recuperer les infos en l'etat normal par les autre
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



    #retourn id de user
    def getId(self):

       return self.id

    # retourne le pseudo de user
    def getPseudo(self):

        return self.pseudo

    #retourne l'etat connect du user
    def getConn(self):

        return self.conn

    # initial l'etat de user on 0 1 2
    #           0 = out
    #            1 = online
    #            2 = sleeping
    def getState(self):

        if self.state == 0 :
            return "is out"
        elif self.state == 1 :
            return "is online"
        elif self.state == 2 :
            return "is sleeping"
    # retourner l'etat en chiffre 0 1 2
    def getNumState(self):

        return self.state
    # retourne l'etat priver parmi les users actifs
    def getUsersPrivate(self):

        return self.usersPrivate

    # attant pour devenir le client priver
    def getUsersWBP(self):

        return self.usersWilldBecomePrivate

    # sleep etat
    def sleep(self):

        if self.state == 1:
            self.state = 2
            return "You are now sleeping"
        else:
            return "Sleep mode is impossible"
    #client revient actif
    def wake(self):

        if self.state == 2:
            self.state = 1
            return "You are back in the chat"
        else:
            return "Wake mode is impossible"
    # le client change de pseudo
    def logchange(self, newPseudo):

        self.pseudo = newPseudo
        return "Congrats, your new pseudo is " + self.pseudo

    # pour activer l'etat d'echange dans l'etats priver,si l'autre client accept ces command,le message
    # ne transfere que le client priver,le message ne sera pas envoye a le client normal
    def private(self, userDest):

        if self in userDest.getUsersWBP() :
            return "Your request has been sent, please wait the answer"
        elif self in userDest.getUsersPrivate() :
            return "Conversation is steal alive with " + userDest.getPseudo()
        else :
            return ""

    # Le enduser autorise un autre user a communiquer avec lui en private
    def acceptpc(self, userEm):

        if userEm in self.usersWillBecomePrivate :
            self.usersWouldBecomePrivate.remove(userEm)
            self.usersPrivate.append(userEm)
            userEm.getUsersPrivate().append(self)
            return "Now, you can speak to '" + userEm.getPseudo() + "' in private with :  " + userEm.getPseudo() + "<msg>"

        return ""

    def denypc(self, userEm):
        '''
            Le user interdit un autre user a communiquer avec lui en "private"
        '''

        if userEm in self.usersWouldBecomePrivate :
            self.usersWouldBecomePrivate.remove(userEm)
            return "You have denied the request of private conversation"

        return ""
    # metter la connection a la fin pendant ceux qui sont dans l'etat prive
    def stoppc(self, otherUser):

        if otherUser in self.getUsersPrivate() :
            self.usersPrivate.remove(otherUser)
            otherUser.getUsersPrivate().remove(self)
            return "End of conversation with '" + otherUser.getPseudo() + "'"

        return ""



    #quit
    def OnQuit(self):
        self.top.quit()
        self.ChatClitSock.close()


    #About
    def OnAbout(self):
        pass

    #mult
    #def mutiThread(self):
    #    threading.Thread.start_new_thread(self.SocketProc_recv,())

def main():
    pp=DNCclitGUI()
    #pp.mutiThread()
    mainloop()

if __name__=='__main__':
    main()

