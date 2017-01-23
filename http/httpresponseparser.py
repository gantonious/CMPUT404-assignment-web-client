import shlex
from http.httpresponse import HttpResponse

class HttpResponseParser:
    def parse(self, serailized_response):
        state = 0
        response = None
        body = ""

        for line in serailized_response.split("\r\n"):
            if state == 0:
                response = self._parse_respone_line(line)
                state = 1
            elif state == 1:
                if line.strip() == "":
                    state = 2
                else:
                    self._parse_header_line(line, response)
            elif state == 2:
                if line != "\r\n":
                    body += line + "\n"
        
        response.with_body(body.strip())
        return response
                
    def _parse_respone_line(self, request_line):
        response_tokens = request_line.split(" ", 2)
        return HttpResponse(response_tokens[1], response_tokens[2])
    
    def _parse_header_line(self, header_line, response):
        colon_index = header_line.index(":")
        header_key = header_line[:colon_index].strip()
        header_value = header_line[colon_index + 1 :].strip()
        
        response.with_header(header_key, header_value)