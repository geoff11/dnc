
class user:
    
    '''
    Classe user : utilisateur du chat
    '''
    
    def __init__(self, id, pseudo, mdp, port):
        '''
            Initialisation du user
        '''
          
        self.id = id 
        self.pseudo = pseudo
        self.mdp = mdp
        self.port = port
        
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
    
    
    def getMdp(self):
        '''
        Methode : retourne le mdp du user
        '''
        return self.mdp
    
     
    def getPort(self):
        '''
        Methode : retourne le port du user
        '''
        return self.port
    
    
    """"""""""""""""""""""""""""""
    #RFC
    
    def list(self):
    
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