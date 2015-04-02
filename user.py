
class user:
    
    '''
    Classe user : utilisateur du chat
    '''
    
    def __init__(self, id, pseudo, port, state = None):
        '''
            Initialisation du user
        '''
          
        self.id = id 
        self.pseudo = pseudo
        self.port = port
        
        if state :
            self.state = state
        else
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
    
     
    def getPort(self):
        '''
        Methode : retourne le port du user
        '''
        return self.port
    
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
        
    def wake(self):
    
    def logchange(self):
    
    def private(self):
    
    def acceptpc(self, port):
        # penser au port du user
    
    def denypc(self):
         
    def stoppc(self):
   
    def filesend(self):
        
    def fileacc(self):
        
    def fileden(self):
        
    """"""""""""""""""""""""""""""