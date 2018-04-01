#receiver program

import socket
import time
import sys


#data = 1234
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((sys.argv[1],int(sys.argv[2]))) #(sys.argv[1],int(sys.argv[2]))	(socket.gethostname(),8080)
sock.listen(3)

while True:
	conn, addr = sock.accept()
	data = conn.recv(2048)
	conn.close()
	print "received: ",data
