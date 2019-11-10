# -*- coding:utf-8 -*-

from __future__ import print_function

from http.server import HTTPServer
from http.server import CGIHTTPRequestHandler

port = 6006

httpd=HTTPServer(('',port),CGIHTTPRequestHandler)
print("Starting simple_http on port:"+str(httpd.server_port))
httpd.serve_forever()
