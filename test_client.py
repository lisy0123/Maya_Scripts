import maya.cmds as cmds
from socket import *

class SocketInfo():
    HOST='172.30.1.48'
    PORT=9999
    ADDR=(HOST, PORT)

clientSocket=socket(AF_INET, SOCK_STREAM)
clientSocket.connect(SocketInfo.ADDR)

print("Connect...")
clientSocket.send("Maya".encode("utf-8"))

data = clientSocket.recv(1024)
print("Data: "+data.decode("utf-8"))

win=data.decode("utf-8")
cmds.window(win, t=win)
cmds.showWindow(win)

clientSocket.close()

