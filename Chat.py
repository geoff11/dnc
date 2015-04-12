import User

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
    
    
    def addClient(self, pseudo):
        client = User.User(len(self.listeClients)+1, pseudo, 1)
        self.listeClients.append(client)
        return client
    
    def deleteClient(self, client):
        self.listeClients.remove(client)
        
    
    def list(self):
        '''
            liste des pseudos connectes
        '''
        
        all_user = ""
        for u in self.listeClients :
             all_user += " " + u.pseudo.decode()
        return all_user
    
    def quit(self, user, msgPerso = None):
        if msgPerso:
            return " leaved the chat saying : " + msgPerso
        else:
            return " leaved the chat"
    
    def sleep(self, user, msgPerso = None):
        if msgPerso:
            return " is sleeping saying : " + msgPerso
        else:
            return " is sleeping"