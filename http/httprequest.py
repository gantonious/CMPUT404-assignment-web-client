# Copyright 2013 Abram Hindle, Eddie Antonio Santos, George Antonious
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

# from https://github.com/gantonious/CMPUT404-assignment-webserver/blob/15b724ee57a2e7a7f89048fbcd2ea5b17bfc5b32/server.py#L33
# modified on February 5 2017

class HttpRequest:
    def __init__(self, method, path):
        self._method = method
        self._path = path
        self._headers = {}
        self._body = ""

    def with_header(self, key, value):
        self._headers[key] = value
        return self
    
    def with_body(self, body):
        self._body = body
        self.with_header("Content-Length", len(body))
        return self

    def method(self):
        return self._method

    def path(self):
        return self._path

    def headers(self):
        return self._headers
    
    def header(self, key):
        if key in self.headers():
            return self.headers()[key]
        return None
    
    def body(self):
        return self._body

    def has_body(self):
        return not len(self._body)

    def __str__(self):
        return self.serialize()

    def serialize(self):
        return self._build_request_line() + \
               self._build_header_lines() + \
               self._build_body_line()

    def _build_request_line(self):
        return "{0} {1} HTTP/1.1".format(self.method(), self.path())

    def _build_header_lines(self):
        header_lines = ["{0}: {1}".format(k, v) for k, v in self._headers.iteritems()]

        if header_lines:
            return "\r\n" + "\r\n".join(header_lines)
        return ""

    def _build_body_line(self):
        if self._body:
            return "\r\n\r\n{0}\r\n".format(self._body)
        return "\r\n\r\n"