from socket import *

class SocketInfo():
	HOST=HOSTNUM
	PORT=PORTNUM
	ADDR=(HOST, PORT)

severSocket=socket(AF_INET, SOCK_STREAM)
severSocket.bind(SocketInfo.ADDR)
severSocket.listen(1)

connectionSocket, addr = severSocket.accept()
print(str(addr),"Connect...")

data = connectionSocket.recv(1024)
print(data.decode("utf-8"))
connectionSocket.send('Testing'.encode("utf-8"))

severSocket.close()
