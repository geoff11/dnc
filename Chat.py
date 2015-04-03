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
    
    
    def identifierClient(self, ip, port, pseudo):
        '''
            Identification du client, renvoi un objet client instancié ou 0 si pseudo deja utilise
        '''
        
        for guy in self.listeClients :
            if guy.pseudo == pseudo :
                return 0
        
        client = User.User(len(self.listeClients)+1, pseudo, ip, port, 1)
        self.listeClients.append(client)
        return client
        
    
    def list(self):
        '''
            liste des pseudos connectes
        '''
        
        all_user = ""
        for u in self.listeClients :
             all_user += u.pseudo
        return all_user
    
    def quit(self, pseudo, msgPerso=""):
        return pseudo.decode() + " leaved the chat" + msgPerso