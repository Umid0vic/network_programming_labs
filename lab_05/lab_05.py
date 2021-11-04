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
		#TODO