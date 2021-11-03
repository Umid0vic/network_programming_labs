# Network programming lab 4 - Sockets: Rock-paper-scissors
# created by Osman Said 2021-11-02

import socket

def server_side():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('localhost', 60003))
	s.listen(1)

	while True
		print('\n Listening...\n')
		(s, addr) = accept()
		print('connection from {}' .format(addr))
		serverPoints = 0
        clientPoints = 0
        while True:
        		#TODO

def client_side():
	socketC = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socketC.connect((host,60003))
    serverPoints = 0
    clientPoints = 0
    while True:
    	#TODO