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

# from https://github.com/gantonious/CMPUT404-assignment-webserver/blob/15b724ee57a2e7a7f89048fbcd2ea5b17bfc5b32/server.py#L100
# modified on February 5 2017

class HttpResponse:
    def __init__(self, response_code, response_message):
        self.code = response_code
        self.message = response_message
        self.headers = {}
        self.body = ""

    def with_header(self, key, value):
        self.headers[key] = value
        return self
    
    def with_body(self, body):
        self.body = body
        return self

    def response_code(self):
        return self.code

    def response_message(self):
        return self.message

    def has_header(self, key):
        return key in self.headers

    def header(self, key):
        if key in self.headers:
            return self.headers[key]
        return None

    def __str__(self):
        return self.serialize()

    def serialize(self):
        return self._build_response_line() + \
               self._build_header_lines() + \
               self._build_body_line()

    def _build_response_line(self):
        return "HTTP/1.1 {0} {1}".format(self.response_code(), self.response_message())
    
    def _build_header_lines(self):
        header_lines = ["{0}: {1}".format(k, v) for k, v in self.headers.iteritems()]

        if header_lines:
            return "\r\n" + "\r\n".join(header_lines)
        return ""

    def _build_body_line(self):
        if self.body:
            return "\r\n\r\n{0}\r\n".format(self.body)
        return "\r\n\r\n"