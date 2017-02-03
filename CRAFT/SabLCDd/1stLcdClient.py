'''
Created on 14 Jul 2012

@author: Jamie
'''
import socket
from time import sleep

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('192.168.2.49', 13666))

sock.send("hello\n")

print sock.recv(1024)

sock.send("client_set name simpleClient\n")
print sock.recv(1024)
sock.send("screen_add myscreen\n")
print sock.recv(1024)
sock.send("widget_add myscreen one string\n")
sock.send("widget_add myscreen two string\n")
sock.send("widget_add myscreen three string\n")
sock.send("widget_add myscreen four string\n")
print sock.recv(1024)
sock.send("widget_set myscreen one 1 1 {Millie Jackson}\n")
sock.send("widget_set myscreen two 1 2 {Smells of Poo}\n")
sock.send("widget_set myscreen three 1 3 {If you kiss her}\n")
sock.send("widget_set myscreen four 1 4 {You will too!}\n")
print sock.recv(1024)

sleep(3)

sock.close( )

print "Did it work?"