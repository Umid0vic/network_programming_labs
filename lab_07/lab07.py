# Network programming lab 7 - Multiple clients
# craeted by Osman Said 01-12-2021

import socket
import select

port = 60003
sockL = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockL.bind(("",port))
sockL.listen(1)
listOfSockets = [sockL]
print("Listening on port{}".format(port))
while True:
    tup = select.select(listOfSockets, [], [])
    sock = tup[0][0]
    if sock==sockL:
        sockClient, addr = sockL.accept()
        listOfSockets.insert(len(listOfSockets),sockClient)
        for c in range(1,len(listOfSockets)):
            if listOfSockets[c] != sockClient:
                listOfSockets[c].sendall(bytearray(("{} connected".format(addr)),'ascii'))
    else:
        data = sock.recv(2048)
        if not data:
            listOfSockets.remove(sock)
            print("{} disconnected".format(sock.getpeername())) 
            for c in range(1,len(listOfSockets)):
                if listOfSockets[c] != sock:
                    listOfSockets[c].sendall(bytearray(("{}: disconnected".format(sock.getpeername())),'ascii'))  

            sock.close()
            for c in range(1,len(listOfSockets)):
                if listOfSockets[c] == sock:
                   listOfSockets.pop(c)
    
        else:
            data=data.decode()
            for c in range(1,len(listOfSockets)):
                listOfSockets[c].sendall(bytearray(("{}: {}".format(sock.getpeername(),data)),'ascii'))
            
            
