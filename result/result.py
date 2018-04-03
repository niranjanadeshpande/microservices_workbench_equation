#receiver program

import socket
import time
import sys
import select



#data = 1234
#socks = [sys.argv[2],sys.argv[3]]



#socks = [1,50]
result =0 
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
		

	result += float(data_square) + float(data_round)
	print "Result is: ", result
	

conn_round.close()
conn_square.close()
'''

import socket
import threading

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    # Set the response to echo back the recieved data 
                    response = data
                    client.send(response)
                else:
                    raise error('Client disconnected')
            except:
                client.close()
                return False

if __name__ == "__main__":
    while True:
        port_num = input("Port? ")
        try:
            port_num = int(port_num)
            break
        except ValueError:
            pass

    ThreadedServer('',port_num).listen()
'''

