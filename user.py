
class user:
    
    '''
    Classe user : utilisateur du chat
    '''
    
    def __init__(self, id, nom, prenom, adresse, mail, tel, nbFreq):
        '''
            Initialisation du user
        '''
          
        self.id = id 
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.mail = mail
        self.tel = tel
        self.nbFrequentations = nbFreq
        
        
    def getId(self):
        '''
        Methode : retourne l'id user
        '''
        return self.id
    
    def getNom(self):
        '''
        Methode : retourne le nom du user
        '''
        return self.nom
    
    
    
    def getPrenom(self):
        '''
        Methode : retourne le prenom du user
        '''
        return self.prenom
    
     
    def getMail(self):
        '''
        Methode : retourne le mail du user
        '''
        return self.mail
    
    
    def getTel(self):
        '''
        Methode : retourne le tel du user
        '''
        return self.tel
    
    
    def getAdresse(self):
        '''
        Methode : retourne l adresse du user
        '''
        return self.adresse    
    
    
    def getNbFrequentations(self):
        '''
        Methode : retourne le nb de frequentations du user
        '''
        return self.nbFrequentations
    