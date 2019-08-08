#!/usr/bin/env python
# -*- coding: utf-8 -*-
          
import sys
import socket              
 
arglen=len(sys.argv)
if arglen<3:
    print('please run as python TCPclient.py <ip_address> <numbers>')
    exit()
data=str()
data=data+str(sys.argv[2])
for i in range(3,arglen):
    data=data+':'+str(sys.argv[i])
 
s = socket.socket()        
 
port = 5000          
# (160, 1, 6, 81, 215, 62, 213, 80, 4, 0, 0, 1, 0)
# a0010651d73ed5500400000100
data = "\xA0\x01\x06\x51\xD7\x3E\xD5\x50\x04\x00\x00\x01\x00"
s.connect((sys.argv[1], port))
s.send(data)
print s.recv(1024)
s.close 