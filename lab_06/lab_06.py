# Network programming lab 6 - HHTP request
# craeted by Osman Said 07-11-2021
import socket


port = 8080
host = ''
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(10)

#establish connection with client
while True:
    print('\n...listning..\n')
    c, addr= sock.accept()
    data= c.recv(1024)
    data = data.decode()

    print(data)
    c.sendall(bytearray('HTTP/1.1 200  ok\n', 'ASCII') )
    c.sendall(bytearray('''
        <html>
        <body>
        <h1>Youre Browser sent the Folowing Request:</h1>
        <pre>''' ,'ASCII'))
    c.send(bytearray(data,'ASCII'))
    c.send(bytearray('''
        </pre>       
        </body>
        </html>
        ''','ascii'))
  
    c.close()
sock.close()