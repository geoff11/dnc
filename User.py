
class User:
    
    '''
    Classe User : utilisateur du chat
    '''
    
    def __init__(self, id, pseudo, ip, port, state = None):
        '''
            Initialisation du user
        '''
          
        self.id = id 
        self.pseudo = pseudo
        self.ip = ip
        self.port = port
        self.adr = str(ip) + " " + str(port)
        
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
    
    def getIp(self):
        '''
        Methode : retourne l ip du user
        '''
        return self.ip
     
    def getPort(self):
        '''
        Methode : retourne le port du user
        '''
        return self.port
    
    def getAdr(self):
        '''
        Methode : retourne l adresse du user
        '''
        return self.adr
    
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
    
    """"""""""""""""""""""""""""""
    #RFC
    
    def quit(self):
        '''
            le client met fin à la connexion
        '''
        
        return "Vous avez ete correctement deconnecte"
        
    def sleep(self):
        '''
            le client reste connecte, mais ne reçoit plus les messages
        '''
           
    def wake(self):
        '''
            le client qui etait « sleep » redevient actif
        '''
        
    def logchange(self, newPseudo):
        '''
            le client change de pseudo
        '''
    
    def private(self, pseudoDest):
        '''
            le client met en place un echange prive avec le client ayant le pseudo indique.
            Le destinataire (pseudo) peut autoriser ou non cet echange.
            S’il l’accepte et jusqu’au message /cmd7 emis par l’une des deux parties,
            les messages entre ces deux clients ne seront plus diffuses aux autres.
        '''
    
    def acceptpc(self, pseudoDest):
        '''
            Le user autorise un autre user a communiquer avec lui en "private"
        '''
    
    def denypc(self, pseudoDest):
        '''
            Le user interdit un autre user a communiquer avec lui en "private"
        '''
         
    def stoppc(self, pseudoDest):
        '''
            Le user met fin aux conversations "private"
        '''
   
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