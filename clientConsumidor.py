#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://localhost:1235/")
print "Consumidor conectado a porta 1235..."
print proxy

proxy.consumir().data
