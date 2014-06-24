#!/usr/bin/python

import socket

f = open('alive_server.conf', 'r') # open config file.
address = f.readline() #read address
port = f.readline() #read port
f.close() #close file.
add = address.strip() #string readlines
prt = port.strip()
s = socket.socket() #open socket
s.bind ((add,int(prt)))
print "Starting server on: {0} {1}".format(add,prt)
s.listen(5)
while True:
    c, caddr = s.accept()
    print "Connection received"
    print "Connection: {0}".format(c)
    print "Address: {0}".format(caddr)

