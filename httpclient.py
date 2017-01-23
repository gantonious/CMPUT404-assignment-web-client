#!/usr/bin/env python
# coding: utf-8
# Copyright 2016 Abram Hindle, https://github.com/tywtyw2002, and https://github.com/treedust
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Do not use urllib's HTTP GET and POST mechanisms.
# Write your own HTTP GET and POST
# The point is to understand what you have to send and get experience with it

import sys
import socket
import re
# you may use urllib to encode data appropriately
import urllib

from http.httprequesttypes import *
from http.httpresponse import HttpResponse
from http.httpresponseparser import HttpResponseParser

def help():
    print "httpclient.py [GET/POST] [URL]\n"

class HTTPClient:
    def __init__(self):
        self._http_response_parser = HttpResponseParser()

    def establish_socket(self, http_request):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.settimeout(1)

        try:
            server_socket.connect((http_request.host_address(), http_request.host_port()))
        except Exception, e:
            # TODO: find appropriate constant
            if e.errno == 8:
                print("Could not resolve hostname: {0}".format(http_request.host_address()))
                sys.exit()

        return server_socket

    def execute(self, http_request):
        server_socket = self.establish_socket(http_request)
        raw_http_request = http_request.serialize()

        server_socket.send(raw_http_request)
        raw_http_response = self.recvall(server_socket)
        http_response = self._http_response_parser.parse(raw_http_response)

        server_socket.close()

        return http_response

    # read everything from the socket
    def recvall(self, sock):
        buffer = bytearray()
        done = False
        while not done:
            try:
                part = sock.recv(1024)
            except:
                part = None
            if (part):
                buffer.extend(part)
            else:
                done = not part
        return str(buffer)

    def GET(self, url, args=None):
        request = GetRequest(url)
        return self.execute(request)

    def POST(self, url, args=None):
        request = PostRequest(url)
        return self.execute(request)

    def command(self, url, command="GET", args=None):
        if (command == "POST"):
            return self.POST( url, args )
        else:
            return self.GET( url, args )
    
if __name__ == "__main__":
    client = HTTPClient()
    command = "GET"
    if (len(sys.argv) <= 1):
        help()
        sys.exit(1)
    elif (len(sys.argv) == 3):
        print client.command( sys.argv[2], sys.argv[1] )
    else:
        print client.command( sys.argv[1] )   
