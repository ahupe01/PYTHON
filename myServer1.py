#!/usr/bin/env python
'''
Server: server should accept incoming connections from client
        and expect to receive data in the format described,
        One word per line.
        Once the server has received the content of the file,
        the server should simply print out a count of the number
        of times each word appears. The words should be displayed
        in sorted (alphabetic) order.
        ** server needs to be run first **
'''

import socket

'''
wordCount function reads the contents that have been sent from the client
and sorts them into alphabetical order, and counts the number of times each
entry is in the contents
'''
def wordCount(data):
    
    wordDict = {}
    
    for i in range(len(data)):

        if wordDict.has_key(data[i]):
            
            wordDict[data[i]] += 1

        else:
            wordDict[data[i]] = 1

    sorted = wordDict.items()
    sorted.sort()

    print "The word count for the file: "
    for k, v in sorted:
        print k, v

'''
main program where we create the bind port and ip and allow the server
to listen on the port. 
'''
import socket
bind_ip="0.0.0.0"
bind_port=50007
sentinel = False

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(1)

print "Listening on host %s: port %d" % (bind_ip, bind_port)
'''
client and server are connected now and the server is ready to accept
data being sent from the client
'''
connection,addr=server.accept()
print 'Connected by', addr

request = connection.recv(1024)
'''
for as long as the contents are being recieved from the client, the string
of data will be concatenated
'''
data = request
while ((len(request)) > 0):
    request = connection.recv(1024)
    if (len(request) > 0):
        data = data + request
'''
split the data
'''
nData = str.split(data, '\n')

'''
call on the wordCount function
'''
wordCount(nData)


        

server.close()
