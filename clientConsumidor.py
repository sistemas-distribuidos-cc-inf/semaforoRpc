#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://localhost:1235/")
proxy.consumir()