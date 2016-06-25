#!/usr/bin/env python
'''
Server: server should accept incoming connections from client
        and expect to receive data in the format described,
        One word per line.
        Once the server has received the content of the file,
        the server should simply print out

'''
'''
functions
'''
import socket
import os
import base64
import hashlib
userDict = {}

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
reads the user "database" file and creates a dictionary
for the contents. the contents are sorted into the username
as a key and the Base 64 encoded salt as the 1st element
and the Base 64 encoding of the user password
concatenated with the salt as the 2nd element
'''
def read_in_file():
    
    with open ('password.txt') as passWordFile:       
        line = passWordFile.read()       
        user = line.strip().split('\n')       
        for each in user:
            (user,userSalt64, passHash)=each.split(':')
            userDict[user] = [userSalt64, passHash]

    passWordFile.close()

'''

'''
def convert(request):
    data = request
    while ((len(request)) > 0):
        request = connection.recv(1024)
        if (len(request) > 0):
            data = data + request
    nData = str.split(data, '\n')
    wordCount(nData)

'''
main program
connection process
'''

bind_port=50007
sentinel = False

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', bind_port))
server.listen(1)

print "Listening on host %s: port %d" % ('', bind_port)
connection,addr=server.accept()
print 'Connected by', addr
credentials = connection.recv(256)
'''
split credentials into attempted username and password
'''
userName, passTry = [x.strip() for x in credentials.split(':')]
'''
call read_in_file function
'''
read_in_file()
'''
user/password verification
'''
if userDict.get(userName):
    userSalt64 = (userDict[userName][0])
    userSalt = base64.b64decode(userSalt64)
    
    hashObj=hashlib.sha256()
    hashObj.update(passTry)
    hashObj.update(userSalt)
    hashDigest=hashObj.digest()
    passHash = base64.b64encode(hashDigest)
    userSalt64 = base64.b64encode(userSalt)
        
    if passHash == (userDict[userName][1]):
        print "Login successful"
        request = connection.recv(1024)
        convert(request)

    else:
        print "incorrect login info"
else:
    print "Username not in database"

'''
close server
'''
server.close()
