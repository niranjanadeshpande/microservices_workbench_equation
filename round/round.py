#receiver program

import socket
import time
import sys


#data = 1234


sock_new = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_new.bind((sys.argv[1],int(sys.argv[2])))
sock_new.listen(10)
sock_new.settimeout(300)

while True:
	conn, addr = sock_new.accept()
	data = conn.recv(2048)
	conn.close()
	print "received: ",data

	
	res = int(round(float(data)))
	data_send = "%s" % res
	print "calculated round", data_send
	
	sock_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock_send.connect((sys.argv[3],int(sys.argv[4])))
	sock_send.settimeout(300)
	sock_send.send(data_send)
	sock_send.close()
	
