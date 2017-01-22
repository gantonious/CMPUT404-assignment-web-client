# from https://github.com/gantonious/CMPUT404-assignment-webserver/blob/master/http/httprequest.py
# modfied on January 22

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