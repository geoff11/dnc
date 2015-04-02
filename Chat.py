import User
from IPython.core.tests.test_inputsplitter import pseudo_input

class Chat:
    
    '''
    Classe Chat : gere les differentes actions du user
    '''
    
    def __init__(self):
        '''
            Initialisation du chat
        '''
        self.listeClients = []
    
    def identifierClient(self, port, pseudo):
        for guy in listeClients :
            if guy.pseudo == pseudo :
                return 0
        
        client = User(self.listeClients.length, pseudo, port, 1)
        self.listeClients.append(client)
        return client
        
    
    def list(self):
        all_user = ""
        for u in listeClients :
             all_user += u.pseudo
        return all_user