#!/usr/bin/python
# -*- coding: utf-8 -*-

import xmlrpclib
import time

millis = time.time()
proxy = xmlrpclib.ServerProxy("http://localhost:1235/")
proxy.produzir(millis)