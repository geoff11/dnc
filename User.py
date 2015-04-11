
class User:
    
    '''
    Classe User : utilisateur du chat
    '''
    
    def __init__(self, id, pseudo, canal, state = 0): #User offline par defaut
        '''
            Initialisation du user
        '''
          
        self.id = id 
        self.pseudo = pseudo
        self.canal = canal # thread
  
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
    
    
    def getState(self):
        '''
        Methode : retourne l etat du user
                0 = out
                1 = online
                2 = sleeping
        '''
        if state == 0 :
            state = self.pseudo + " is out"
        elif state == 1 :
            state = self.pseudo + " is online"
        elif state == 2 :
            state = self.pseudo + " is sleeping"
        elif state == 3 :
            state = self.pseudo + " is online but in private chat"
    
    def getThread(self):
        return self.canal
    
    """"""""""""""""""""""""""""""
    #RFC
    
    def quit(self):
        '''
            le client met fin à la connexion
        '''
        self.state = 0
        return "Vous avez ete correctement deconnecte"
        
    def sleep(self):
        '''
            le client reste connecte, mais ne reçoit plus les messages
        '''
        self.state=2
        return "You are now sleepping"
        # TODO : Implementer le fait que les sleepers ne recoivent plus les messages de sendToAll
           
    def wake(self):
        '''
            le client qui etait « sleep » redevient actif
        '''
        self.state=1
        return self.pseudo+" is back"
        
    def logchange(self, newPseudo):
        '''
            le client change de pseudo
        '''
        oldLog = self.pseudo 
        self.pseudo=newPseudo
        return oldLog + "Changed his log with: "+self.pseudo
    
    def private(self, pseudoDest):
        '''
            le client met en place un echange prive avec le client ayant le pseudo indique.
            Le destinataire (pseudo) peut autoriser ou non cet echange.
            S’il l’accepte et jusqu’au message /cmd7 emis par l’une des deux parties,
            les messages entre ces deux clients ne seront plus diffuses aux autres.
        '''
        return self.pseudo + " Wants to chat with you in private. acceptpc/denypc ? "
        
    
    def acceptpc(self, pseudoDest):
        '''
            Le user autorise un autre user a communiquer avec lui en "private"
        '''
        self.state=3 # passe en state "private"
        return "yes"
    
    def denypc(self, pseudoDest):
        '''
            Le user interdit un autre user a communiquer avec lui en "private"
        '''
        return "no"
         
    def stoppc(self, pseudoDest):
        '''
            Le user met fin aux conversations "private"
        '''
        self.state=1
        #TODO : Passer le state du pseudoDest a 1 : impossible avec cette architecture, acces au chat impossible
        return self.pseudo + "is back in public chat"
   
    def filesend(self, pseudoDest, fic, port):
        '''
            le client indique à pseudo qu’il desire lui envoyer un fichier sur un port au choix
        '''
        
    def fileacc(self):
        '''
            le destinataire autorise un transfert de fichier
            Le transfert demarre immediatement (fichier considere comme du binaire)
            Le protocole doit donc gerer la connexion directe entre deux clients (choix du port et du protocole de transfert, notamment)
        '''
        
    def fileden(self):
        '''
            le destinataire annule un transfert de fichier
        '''
        
    """"""""""""""""""""""""""""""