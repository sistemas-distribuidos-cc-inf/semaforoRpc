#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
from scbl import BufferLimitado

b = BufferLimitado()

server = SimpleXMLRPCServer(("localhost", 1235))

def produzir(item):
    b.insert(item)
    print "PRODUTOR. item: ", item , " b.livre: ", b.livre, " b.cheio: ", b.cheio

def consumir():
    item = b.remove()
    print " CONSUMIDOR. item: ", item , " b.livre: ", b.livre, " b.cheio: ",  b.cheio
    return item

server.register_function(produzir, "produzir")
server.register_function(consumir, "consumir")
server.serve_forever()