# from https://github.com/gantonious/CMPUT404-assignment-webserver/blob/master/http/httpresponse.py
# modfied on January 22

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