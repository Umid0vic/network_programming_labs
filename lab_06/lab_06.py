# Network programming lab 6 - HHTP request
# craeted by Osman Said 07-11-2021

port = 8080
host = ''
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))

#establish connection with client
