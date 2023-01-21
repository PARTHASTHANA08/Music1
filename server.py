import socket
from threading import Thread 
IP_ADDRESS = "127.0.0.1"
PORT = 8050
SERVER = None
bufferSize=4096
clients={}

def acceptConnections():
    global SERVER
    global clients
    while True:
        client,addr = SERVER.accept()
        print(client,addr)

def setup():
    print("\n\t\t\t\t\t\tIP MESSENGER")
    global PORT,IP_ADDRESS,SERVER
    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS,PORT))
    SERVER.listen(100)
    print("\t\t\t\t SERVER IS WAITING FOR INCOMING CONNECTIONS \n")
    acceptConnections()

setup_thread = Thread(target=setup)
setup_thread.start()    