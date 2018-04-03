#sender squares

import socket
import time
import sys

N = sys.argv[5]
#res = 7 * 7
#data = "%s" % res
#print "sending ", res

sock_square = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_integral = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_square.connect((sys.argv[1],int(sys.argv[2]))) #socket.gethostname(),5050
sock_integral.connect((sys.argv[3],int(sys.argv[4]))) 
sock_square.settimeout(300)
sock_integral.settimeout(300)

#res = 3 * math.pow(x,3) + math.sin(0.01)
while True:
	#for i in range(0,N):
		#x=i
		#result = i
	data = N
	print "sending ", data
	sock_square.send(data)
	sock_integral.send(data)
		
	#break

sock_square.close()
sock_integral.close()
