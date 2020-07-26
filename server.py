#1.0.4.2
import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
CONN = []
NAME = []

def sender(msg, CONN, conn):
    Final_Msg = msg
    for i in range(0,len(CONN)):        
        msg = ""
        if CONN[i] != conn:
            msg = NAME[CONN.index(conn)] + " : " + Final_Msg
            CONN[i].send(msg.encode(FORMAT))

def Cancel(msg, CONN, conn):
    for i in range(0,len(CONN)):        
        if CONN[i] != conn:
            CONN[i].send(msg.encode(FORMAT))
    

    
def handle_client(conn, addr):
    
    print(f"[NEW CONNECTION] [{addr} as {NAME[CONN.index(conn)]}]  connected.")
    conn.send("Thanks for joining!".encode(FORMAT))
    connected = True
    
    while connected:
        msg = conn.recv(1024).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            msg = "\t" +  NAME[CONN.index(conn)] + " - Disconnected"
            Cancel(msg, CONN, conn)
            NAME.remove(NAME[CONN.index(conn)])
            CONN.remove(conn)
            connected = False
        else:
            sender(msg, CONN, conn)
            print(f"[{addr}] {msg}")

    conn.close()
    print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 3}")
    


def start():
	server.listen()
	print(f"[LISTENING] Server is listening on {SERVER}")
	while True:
		conn, addr = server.accept()
		CONN.append(conn)
		n = conn.recv(1024).decode()
		NAME.append(n)
		thread = threading.Thread(target=handle_client, args= (conn,addr))
		thread.start()
		print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 2}")

	


print("[STARTING...] server is starting")
start()

