
class User:
    
    '''
    Classe User : utilisateur du chat
    '''
    
    def __init__(self, id, pseudo, conn, state = 0): #User offline par defaut
        '''
            Initialisation du user
        '''
          
        self.id = id 
        self.pseudo = pseudo
        self.conn = conn
        self.usersPrivate = [] # liste de users pour les messages privees
        self.usersWouldBecomePrivate = []
        self.usersWouldSendFiles = [] # dictionnaire du type : [{ user1 : fic1}, {user2 : fic2}...]
  
        if state :
            self.state = state
        else :
            self.state = 0
        
    def getId(self):
        '''
        Methode : retourne l'id user
        '''
        return self.id
    
    def getPseudo(self):
        '''
        Methode : retourne le pseudo du user
        '''
        return self.pseudo
    
    def getConn(self):
        '''
        Methode : retourne le thread du user
        '''
        
        return self.conn
    
    def getState(self):
        '''
        Methode : retourne l etat du user
                0 = out
                1 = online
                2 = sleeping
        '''
        if self.state == 0 :
            return "is out"
        elif self.state == 1 :
            return "is online"
        elif self.state == 2 :
            return "is sleeping"
    
    def getNumState(self):
        '''
        Methode : retourne l etat du user sous forme numerique : 0,1,2
        '''
        return self.state
    
    def getUsersPrivate(self):
        '''
        Methode : retourne les users privees en communication avec le user actif
        '''
        return self.usersPrivate
    
    def getUsersWBP(self):
        '''
        Methode : retourne les users privees voulant etre en communication privee avec le user actif
        '''
        return self.usersWouldBecomePrivate
    
    def getUsersWSF(self):
        '''
        Methode : retourne les users voulant envoyer des fichiers au user actif
        '''
        return self.usersWouldSendFiles
    
    """"""""""""""""""""""""""""""
    #RFC
    
    def quit(self):
        '''
            le client met fin à la connexion
        '''
        self.state = 0
        return "/quit"
        
    def sleep(self):
        '''
            le client reste connecte, mais ne reçoit plus les messages
        '''
        if self.state == 1:
            self.state = 2
            return "You are now sleeping"
        
        return "Sleep mode is impossible"
           
    def wake(self):
        '''
            le client qui etait « sleep » redevient actif
        '''
        if self.state == 2:
            self.state = 1
            return "You are back in the chat"
    
        return "Wake mode is impossible"   
        
    def logchange(self, newPseudo):
        '''
            le client change de pseudo
        '''
        
        self.pseudo = newPseudo
        return "Congrats, your new pseudo is " + self.pseudo
    
    def private(self, userDest):
        '''
            le client met en place un echange prive avec le client ayant le pseudo indique.
            Le destinataire (pseudo) peut autoriser ou non cet echange.
            S’il l’accepte et jusqu’au message /cmd7 emis par l’une des deux parties,
            les messages entre ces deux clients ne seront plus diffuses aux autres.
        '''
        
        
        if self in userDest.getUsersWBP() or userDest in self.usersWouldBecomePrivate :
            return "Your request was already sent, please wait the answer"
        elif self in userDest.getUsersPrivate() :
            return "Conversation is steal alive with " + userDest.getPseudo()
        else :
            return ""
        
    
    def acceptpc(self, userEm):
        '''
            Le userDest autorise un autre user a communiquer avec lui en "private"
        '''
        
        if userEm in self.usersWouldBecomePrivate :
            self.usersWouldBecomePrivate.remove(userEm)
            self.usersPrivate.append(userEm)
            userEm.getUsersPrivate().append(self)
            return "Now, you can speak to '" + userEm.getPseudo() + "' in private with : /mp " + userEm.getPseudo() + "<msg>"
        
        return ""
    
    def denypc(self, userEm):
        '''
            Le user interdit un autre user a communiquer avec lui en "private"
        '''
        
        if userEm in self.usersWouldBecomePrivate :
            self.usersWouldBecomePrivate.remove(userEm)
            return "You have denied the request of private conversation"
        
        return ""
         
    def stoppc(self, otherUser):
        '''
            Le user met fin a une conversation "private" avec un autre user
        '''
        
        if otherUser in self.usersPrivate :
            self.usersPrivate.remove(otherUser)
            otherUser.getUsersPrivate().remove(self)
            return "End of conversation with '" + otherUser.getPseudo() + "'"
        
        return ""
    
    def mp(self, otherUser):
        '''
            Le user envoi un message privee a l autre user, une fois la connexion private etablie
        '''
        
        if otherUser in self.getUsersPrivate() :
            return "MP was sent to '" + otherUser.getPseudo() + "' successfully"
        
        return ""
    
   
    def filesend(self, userDest):
        '''
            le client indique à userDest qu’il desire lui envoyer un fichier sur un port au choix
        '''
        
        if self in userDest.getUsersWSF() :
            return "Your request was already sent, please wait the answer"
        else :
            return ""
        
        
    def fileacc(self, pseudoEm):
        '''
            le destinataire autorise un transfert de fichier
            Le transfert demarre immediatement (fichier considere comme du binaire)
            Le protocole doit donc gerer la connexion directe entre deux clients (choix du port et du protocole de transfert, notamment)
        '''
        
        file = ""
        
        for couple in self.usersWouldSendFiles:
            if couple[pseudoEm]:
                file = couple[pseudoEm]
                coupleASuppr = couple
        
        if file : # if exist
            f = open('file_'+ pseudoEm,'wb') #open in binary
            f.write(file)
            f.close()
            #del self.usersWouldSendFiles[userEmd]
            self.usersWouldSendFiles.remove(coupleASuppr)
            return "File download with success !"
        
        return ""
    
        
    def fileden(self, pseudoEm):
        '''
            le destinataire annule un transfert de fichier
        '''
        
        file = ""
        
        for couple in self.usersWouldSendFiles:
            if couple[pseudoEm]:
                file = couple[pseudoEm]
                coupleASuppr = couple
        
        if file : # if exist
            #del self.usersWouldSendFiles[userEmd]
            self.usersWouldSendFiles.remove(coupleASuppr)
            return "You have denied the download"
        
        return ""
        
        
    """"""""""""""""""""""""""""""