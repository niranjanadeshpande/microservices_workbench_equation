#sender squares

import socket
import time
import sys
import math

res = 0.0
sock_new = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_new.bind((sys.argv[1],int(sys.argv[2])))
sock_new.listen(1000)
sock_new.settimeout(300)

while True:

	conn, addr = sock_new.accept()
	data = conn.recv(2048)

	print "received: ",data
	N = int(float(data))
	
	for x in range(0,N):
		res += 3 * math.pow(x,3) + math.sin(0.01)

	data = "%s"% res
	print "Sending ",res
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((sys.argv[3],int(sys.argv[4]))) #socket.gethostname(),5050
	sock.settimeout(300)
	sock.send(data)
sock.close()
conn.close()
#res = 3 * math.pow(x,3) + math.sin(0.01)
