#receiver program

import socket
import time
import sys
import select



#data = 1234
#socks = [sys.argv[2],sys.argv[3]]



#socks = [1,50]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


sock_round = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_square = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock_round.setblocking(0)
sock_square.setblocking(0)

sock_round.bind((sys.argv[1],int(sys.argv[2]))) #(sys.argv[1],int(sys.argv[2]))	(socket.gethostname(),8080)
sock_square.bind((sys.argv[1],int(sys.argv[3])))

sock_round.listen(10)
sock_square.listen(10)

sock_round.settimeout(500)
sock_square.settimeout(500)
'''


while True:
    # this will block until at least one socket is ready
    ready_socks,_,_ = select.select(socks, [], []) 
    for sock in ready_socks:
	sock.settimeout(600)
        data, addr = sock.recvfrom(1024) # This is will not block
        print "received message:", data
	x = data + x
    print "x, ",x
	
'''
while True:

	conn_round, addr_round = sock_round.accept()
	conn_square, addr_square = sock_square.accept()
	data_round = conn_round.recv(2048)
	data_square = conn_square.recv(2048)	

	if data_square!='':
		print "received from square: ",data_square
	if data_round!='':
		print "received from round: ",data_round
	else:
		print "TIMEOUT!!!!"
		
	conn_round.close()
	conn_square.close()
	result = float(data_square) + float(data_round)
	print "Result is: ", result
	

