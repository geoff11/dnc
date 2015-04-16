class Utilisateurs:
    
    '''
    Classe Utilisateurs : personnes inscrits au chat
    '''
    
    def __init__(self, id, pseudo, connexion, etat = 0):
        '''
            Initialisation de l'utilisateur par deffaut
        '''
          
        self.id = id 
        self.pseudo = pseudo
        self.connexion = connexion
        self.private = []
        self.privateSoon = []
  
        if etat :
            self.etat = etat
        else :
            self.etat = 0
        
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
    
    def getConnexion(self):
        '''
        Methode : retourne le thread du user
        '''
        
        return self.connexion
    
    def getEtat(self):
        '''
        Methode : retourne l etat du user
        '''
        if self.etat == 0 :
            return "offline"
        elif self.etat == 1 :
            return "online"
        elif self.etat == 2 :
            return "sleeping"
    
    def getNumEtat(self):
        '''
        Methode : retourne l etat du user sous forme numerique : 0,1,2
        '''
        return self.etat
    
    def getPrivate(self):
        '''
        Methode : retourne les users privees en communication avec le user actif
        '''
        return self.private
    
    def getPrivateSoon(self):
        '''
        Methode : retourne les users privees voulant etre en communication privee avec le user actif
        '''
        return self.privateSoon
    
    def getUsersWSF(self):
        '''
        Methode : retourne les users voulant envoyer des fichiers au user actif
        '''
        return self.sendFiles

    
    def quit(self):
        '''
            le client met fin à la connexion
        '''
        self.etat = 0
        return "/quit"
        
    def sleep(self):
        '''
            le client reste connecte, mais ne reçoit plus les messages
        '''
        if self.etat == 1:
            self.etat = 2
            return "sleeping mode"
           
    def wake(self):
        '''
            le client qui etait « sleep » redevient actif
        '''
        if self.etat == 2:
            self.etat = 1
            return "back in black...in chat" 
        
    def logchange(self, newPseudo):
        '''
            le client change de pseudo
        '''
        
        self.pseudo = newPseudo
        
        return "your new pseudo is " + self.pseudo
    
    def private(self, otherPrivate):
        '''
            le client met en place un echange prive avec le client ayant le pseudo indique.
            Le destinataire (pseudo) peut autoriser ou non cet echange.
            S’il l’accepte et jusqu’au message /cmd7 emis par l’une des deux parties,
            les messages entre ces deux clients ne seront plus diffuses aux autres.
        '''
        
        
        if self in otherPrivate.getPrivateSoon() or otherPrivate in self.privateSoon :
            
            return "Wait a minute for request"
        
        elif self in otherPrivate.getPrivate() :
            
            return "you talking with" + otherPrivate.getPseudo()
        
    
    def accept(self, emissionPrivate):
        '''
            Le userDest autorise un autre user a communiquer avec lui en "private"
        '''
        
        if emissionPrivate in self.privareSoon :
            
            self.privateSoon.remove(emissionPrivate)
            self.private.append(emissionPrivate)
            emissionPrivate.getPrivate().append(self)
            
            return "Now" + emissionPrivate.getPseudo() + "talk in mp with you"
    
    def deny(self, emissionPrivate):
        '''
            Le user interdit un autre user a communiquer avec lui en "private"
        '''
        
        if emissionPrivate in self.privateSoon :
            
            self.privateSoon.remove(emissionPrivate)
            return "refuse the conversation"
         
    def stop(self, otherPrivate):
        '''
            Le user met fin a une conversation "private" avec un autre user
        '''
        
        if otherPrivate in self.private :
            
            self.private.remove(otherPrivate)
            otherPrivate.getPrivate().remove(self)
            
            return "you stop the converstaion with" + otherPrivate.getPseudo() + ""
    
    def mp(self, otherPrivate):
        '''
            Le user envoi un message privee a l autre user, une fois la connexion private etablie
        '''
        
        if otherPrivate in self.getPrivate() :
            return "MP was sent to '" + otherPrivate.getPseudo() + ""
        