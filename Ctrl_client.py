import socket, sys, threading

# Jaune 1 Team -- DNC Client 

if len(sys.argv) != 3:
    print("Usage: {} <ip> <port>".format(sys.argv[0]))
    sys.exit(1)

TAILLE_TAMPON = 1024


welcoming = """
                            #--/        \
                           |   \______   |
                             - ---^^- / /
                                     ||/
                                     |||
                                   .:'':.
                             /^/^^\/     \
                         0___O_\O_/       |
                         |               /
                         |       .._    /
                          \ ____/   |  |               /
                                    |  |             //
                             ^^^^^  |  |            ||
                          ^^^^^^^^^^|  \         __ /|
                         ^^^^^^   ^^|   \       /     \
                         ^^^^^    __|    \____/        |
WELCOME                    ^^^    \    /               |
TO                                 \-/          (_     \
DNC                                  |  |\__________\   |
                                    /|  |          \ \  |
                            _____  | |  |     ______\ \  \
                           /    ____/   |    /    ____/   \
                           \(_ /         \   \(_ /        |
                               \_(____.../       \_(_____/"""


   
# Définition d'un client réseau gérant en parallèle l'émission
# et la réception des messages (utilisation de 2 THREADS).


class ThreadReception(threading.Thread):
    '''
        Classe ThreadReception = objet thread gérant la réception des messages
    '''
    
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn           # réf. du socket de connexion
   
    def run(self):
        #print(welcoming)
        print("Login : ")
        
        while True :
            message_recu = self.connexion.recv(TAILLE_TAMPON).decode()
            print ("*" + message_recu + "*")
            
            if message_recu.lower() == "/quit":
                break
            
        # Le thread <réception> se termine ici.
        # On force la fermeture du thread <émission> :
        th_E._Thread__stop()
        print ("Client stopped. Connexion interrupt.")
        self.connexion.close()
        sys.exit()
        
            
class ThreadEmission(threading.Thread):
    
    '''
        Classe ThreadEmission = objet thread gérant l'émission des messages
    '''
    
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn           # réf. du socket de connexion
   
    def run(self):
        while 1:
            message_emis = input()
            self.connexion.send(message_emis.encode())
            
            
# Programme principal - Établissement de la connexion par socket :
connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = sys.argv[1]
port = int(sys.argv[2])

try:
    connexion.connect((host, port))
except socket.error:
    print ("LConnexion failed")
    sys.exit()    

print ("Connexion OK")
            
# Dialogue avec le serveur : on lance deux threads pour gérer
# indépendamment l'émission et la réception des messages :
th_E = ThreadEmission(connexion)
th_R = ThreadReception(connexion)
th_E.start()
th_R.start()                 