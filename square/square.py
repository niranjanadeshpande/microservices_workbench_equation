#sender squares

import socket
import time
import sys

x = 7
res = 7 * 7
data = "Hello, world! sending... %s" % res
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((sys.argv[1],int(sys.argv[2]))) #socket.gethostname(),5050
sock.send(data)
sock.close()

#res = 3 * math.pow(x,3) + math.sin(0.01)
