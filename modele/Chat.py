from modele import User

class Chat:
    
    '''
    Classe Chat : gere les differentes actions du user
    '''
    
    def __init__(self):
        '''
            Initialisation du chat
        '''
        self.listeClients = [] # TODO : mettre sous forme de dictionnaire ak les connexions
    
    
    def verifLogin(self, pseudo):
        '''
            Verifie si le log est deja attribue : renvoi faux si pseudo deja utilise sinon vrai
        '''
        
        for guy in self.listeClients :
            if guy.pseudo == pseudo :
                return False
        return True
    

    def addClient(self, pseudo, conn):
        client = User.User(len(self.listeClients)+1, pseudo, conn, 1)
        self.listeClients.append(client)
        return client
    
    def deleteClient(self, client):
        self.listeClients.remove(client)
     
    def getClientByPseudo(self, pseudo):
        for guy in self.listeClients :
            if guy.pseudo == pseudo :
                return guy
        return False
    
    def list(self):
        '''
            liste des pseudos connectes
        '''
        
        all_user = ""
        for u in self.listeClients :
             all_user += " " + u.pseudo
        return all_user
    
    def quit(self, user, msgPerso = None):
        if msgPerso:
            return "leaved the chat saying : " + msgPerso
        else:
            return "leaved the chat"
    
    def sleep(self, user, msgPerso = None):
        if user.getNumState() == 1:
            if msgPerso:
                return "is sleeping saying : " + msgPerso
            else:
                return "is sleeping"
        else:
            return ""
    
    def wake(self, user, msgPerso = None):
        if user.getNumState() == 2:
            if msgPerso:
                return "is back on the chat saying : " + msgPerso
            else:
                return "is back"
        else:
            return ""
    
    def logchange(self, user, newPseudo):
        '''
            le client change de pseudo
        '''
        if self.verifLogin(newPseudo):
            oldLog = user.getPseudo()
            return "is the new pseudo of the old " + oldLog
        else :
            return ""
        
    
    def private(self, pseudoEm, pseudoDest):
        '''
            le client met en place un echange prive avec le client ayant le pseudo indique.
            Le destinataire (pseudo) peut autoriser ou non cet echange.
            S’il l’accepte et jusqu’au message /stoppc emis par l’une des deux parties,
            les messages entre ces deux clients ne seront plus diffuses aux autres.
        '''
        
        if not self.verifLogin(pseudoDest) and pseudoDest != pseudoEm : # s il n est pas dispo, c est qu il existe
            
            userEmetteur = self.getClientByPseudo(pseudoEm)
            userDest = self.getClientByPseudo(pseudoDest)
            
            userDest.getUsersWBP().append(userEmetteur)
            return "wants to chat with you in private for the session. /acceptpc "+pseudoEm+" or /denypc "+pseudoEm+" ? "
        
        else :
            return ""
    
    def filesend(self, pseudoEm, pseudoDest, fic):
        '''
            le client tente d envoyer un fichier 
        '''
        
        if not self.verifLogin(pseudoDest) and pseudoDest != pseudoEm : # s il n est pas dispo, c est qu il existe
            
            userEmetteur = self.getClientByPseudo(pseudoEm)
            userDest = self.getClientByPseudo(pseudoDest)
            
            with open(fic, 'rb') as content_file :
                ficBinary = content_file.read()
            
            userDest.getUsersWSF().append({pseudoEm:ficBinary}) # liste de dictionnaire contenant (user, fic)  
                       
            return "wants to share a file with you. /fileacc "+pseudoEm+" or /fileden "+pseudoEm+" ?"
        
        else :
            return ""