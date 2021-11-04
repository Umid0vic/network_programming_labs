# Network programming lab 4 - Sockets: Rock-paper-scissors
# created by Osman Said 2021-11-02

import socket

def server_side():
	socketS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socketS.bind(('localhost', 60003))
	socketS.listen(1)

	while True:
		print('\n Listening...\n')
		(socketC, addr) = socketS.accept()
		print(' connection from {}' .format(addr))
		serverPoints = 0
		clientPoints = 0
		while True:
			s_move = input(' ({},{}) Your move: '.format(serverPoints, clientPoints))
			while s_move not in {'S', 'P', 'R'}:
				s_move = input(' Choose one of the moves (S, P, R): ')
			data = socketC.recv(1024)
			c_move = data.decode('ascii')

			socketC.sendall(bytearray(s_move, 'ascii'))
			print(' (opponent\'s move: {})'.format(c_move))
			if (s_move == 'S' and c_move =='P') or (s_move == 'P' and c_move == 'R') or (s_move == 'R' and c_move == 'S'):
				serverPoints += 1
			elif (s_move == c_move):
				pass
			else:
				clientPoints += 1
			if serverPoints == 10:
				print(' You won {} against {}'.format(serverPoints, clientPoints))
				break
			elif clientPoints == 10:
				print(' You lost {} againts {}'.format(serverPoints, clientPoints))
				break
		socketC.close()
		print(' Client disconnected')



def client_side(host):
	socketC = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	socketC.connect((host,60003))
	serverPoints = 0
	clientPoints = 0
	while True:
		c_move = input(' ({},{}) Your move: '.format(clientPoints, serverPoints))
		while c_move not  in {'S', 'P', 'R'}:
			c_move = input(' Choose one of the moves (S, P, R): ')
		socketC.sendall(bytearray(c_move,'ascii'))
		data = socketC.recv(1024)
		s_move = data.decode('ascii')

		print(' (opponent\'s move: {})'.format(s_move))
		if (c_move == 'S' and s_move == 'P') or (s_move == 'P' and c_move == 'R') or (c_move == 'R' and s_move =='S'):
			clientPoints += 1
		elif (s_move == c_move):
			pass
		else:
			serverPoints += 1
		if clientPoints == 10:
			print(' You won {} against {}'.format(clientPoints, serverPoints))
			break
		elif serverPoints == 10:
			print(' You lost {} againts {}'.format(clientPoints, serverPoints))
			break
	socketC.close()
	print(' You are disconnected from server')
    

while True:
	print(' Welcome to the game!')
	ans = input(' Do you want to be server (S) or client (C): ')
	
	while ans not in {'S', 'C'}:
			ans = input(' Enter (S) for playing server or (C) for client:')
	if ans == 'S':
		server_side()
	else:
		host = input("Enter the server's name or IP: ")
		client_side(host)