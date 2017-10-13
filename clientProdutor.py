#!/usr/bin/python
# -*- coding: utf-8 -*-

import xmlrpclib
import time

millis = time.time()
proxy = xmlrpclib.ServerProxy("http://localhost:1235/")
print "Produtor conectado a porta 1235..."
print proxy

res = proxy.produzir(millis).data
print res



