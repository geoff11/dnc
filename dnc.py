import Utilisateurs

class dnc:
    
    '''
    Classe dnc : gere les differentes actions du user
    '''
    
    def __init__(self):
        '''
            Initialisation du chat
        '''
        self.listePseudo = []
    
    
    def login(self, pseudo):
        '''
            Methode : est ce que le pseudo est deja connecté sur le chat
        '''
        
        for user in self.listePseudo :
            
            if user.pseudo == pseudo :
                
                return False
            
        return True
    

    def addUser(self, pseudo, connexion):
        '''
            Methode : On ajoute un pseudo a la liste
        '''
        
        client = Utilisateurs.Utilisateurs(len(self.listePseudo)+1, pseudo, connexion, 1)
        self.listePseudo.append(client)
        
        return client
    
    def deleteUser(self, client):
        
        self.listePseudo.remove(client)
     
    def getPseudoClient(self, pseudo):
        
        for user in self.listePseudo :
            
            if user.pseudo == pseudo :
                
                return user
            
        return False
    
    def listePseudo(self):
        '''
            Methode : retourne la liste des pseudos connectes
        '''
        
        all_user = ""
        for everyUser in self.listePseudo :
            
            if everyUser.etat!=0:
                
                all_user += " " + everyUser.pseudo
                
        return all_user
    
    def quit(self, user, message):
    
        if message:
            
            return "quit the chat !! " + message
 
    
    def sleep(self, user, message):
        
        if user.getNumState() == 1:
            
            if message:
                
                return "sleeping on chat !! " + message
    
    def wake(self, user, message):
        
        if user.getNumEtat() == 2:
            
            if message:
                return "back on chat !!" + message
    
    def logchange(self, user, newPseudo):
        '''
            le client change de pseudo
        '''
        if self.login(newPseudo):
            
            pseudo = user.getPseudo()
            
            return "new peseudo is : " + pseudo
        
    
    def private(self, emissionPrivate, otherPrivate, pseudoEm=None,userDest=None):
        '''
            le client met en place un echange prive avec le client ayant le pseudo indique.
            Le destinataire (pseudo) peut autoriser ou non cet echange.
            S’il l’accepte et jusqu’au message /stoppc emis par l’une des deux parties,
            les messages entre ces deux clients ne seront plus diffuses aux autres.
        '''
        
        if not self.login(otherPrivate) and otherPrivate != emissionPrivate :
            
            userEmetteur = self.getPseudoClient(emissionPrivate)
            userDestinataire = self.getPseudoClient(otherPrivate)
            
            userDest.getPrivateSoon().append(emissionPrivate)
            return "you want a private conversation. /accept "+pseudoEm+" or /deny "+pseudoEm+" ? "
    