#!/usr/bin/env python
'''
Client: client program should take two arguments
        the first is the port number of the listening server
        and the second is the file path to a data file.
        
        client should then read from the input file and send the contents
        of the file to the server.
        
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
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('',target_port))

'''
Get username and password from user
'''
userName = raw_input("Input username: ")
passWord = raw_input("Input password: ")

'''
send username and password to server
'''
client.send(userName+":"+passWord+"\n")

data = [line.strip() for line in open(target_file, 'r')]

sData = '\n'.join(data)

client.sendall(sData)

print "Sent"

client.close()
