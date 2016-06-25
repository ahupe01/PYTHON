#!/usr/bin/env python
'''
Client: client program should take two arguments
        the first is the port number of the listening server
        and the second is the file path to a data file.
        
        client should read from the input file and send the contents
        of the file to the server.

        The server must be run first and will give the port
        that it is listening on. Once the server is listening
        on the port, the client may be run using the statement
        (on a mac) "python myClient1.py 50007 data.txt"
        
'''

import socket
import sys

'''
declare the target port and file via the system arguments in command line
'''
target_port = int(sys.argv[1])
target_file = sys.argv[2]

check = False
'''
create socket
'''
target_host="localhost"
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))

'''
read stripped string of contents from target file into variable 'data'
'''
data = [line.strip() for line in open(target_file, 'r')]
sData = '\n'.join(data)

'''
send contents to server
'''
client.sendall(sData)
print "Sent"

'''
close client
'''
client.close()
