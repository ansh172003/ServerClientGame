#1.0.4.2
import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = '192.168.42.82'
ADDR = (SERVER, PORT)

temp = []
while temp == []:
    name = input("\tEnter Your name : ")
    temp = name.split()
    name = name.encode(FORMAT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

client.send(name)
print(client.recv(2048).decode())


def sendMsg():   
    while True:
        msg = input("")
        if msg == 'n':
            msg = DISCONNECT_MESSAGE
            message = msg.encode(FORMAT)
            client.send(message)
            break
            
        else:
            message = msg.encode(FORMAT)
            client.send(message)

def send():
    ithread = threading.Thread(target = sendMsg)
    ithread.daemon = True
    ithread.start()

    while True:
        data = client.recv(2048).decode()
        if not data:
            break
        print(data)
send()







        


