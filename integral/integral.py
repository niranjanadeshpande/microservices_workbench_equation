#sender squares

import socket
import time
import sys
import math

x = 7
res = 3 * math.pow(x,3) + math.sin(0.01)
data = "%s"% res
print "Sending ",res
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((sys.argv[1],int(sys.argv[2]))) #socket.gethostname(),5050
sock.settimeout(300)
sock.send(data)
sock.close()

#res = 3 * math.pow(x,3) + math.sin(0.01)
