import User

class Chat:
    
    '''
    Classe Chat : gere les differentes actions du user
    '''
    
    def __init__(self):
        '''
            Initialisation du chat
        '''
        self.listeClients = []
    
    
    def verifLogin(self, ip, port, pseudo):
        '''
            Verifie si le log est deja attribue : renvoi faux si pseudo deja utilise sinon vrai
        '''
        
        for guy in self.listeClients :
            if guy.pseudo == pseudo :
                return False
        return True
    
    
    def addClient(self, ip, port, pseudo):
        client = User.User(len(self.listeClients)+1, pseudo, ip, port, 1)
        self.listeClients.append(client)
        return client
    
    def deleteClient(self, client):
        for u in self.listeClients :
            if u.getPseudo() == client.getPseudo() :
                self.listeClients.remove(u)
        
    
    def list(self):
        '''
            liste des pseudos connectes
        '''
        
        all_user = ""
        for u in self.listeClients :
             all_user += " " + u.pseudo.decode()
        return all_user
    
    def quit(self, user, msgPerso = None):
        self.deleteClient(user)
        if msgPerso:
            return " leaved the chat saying : " + msgPerso
        else:
            return " leaved the chat"