from socket import *

class SocketInfo():
	HOST='172.30.1.48'
	PORT=9999
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
