import shlex
from http.httpresponse import HttpResponse

class HttpResponseParser:
    def parse(self, serailized_response):
        state = 0
        response = None
        body = ""

        for line in serailized_response.split("\n"):
            if state == 0:
                response = self._parse_request_line(line)
                state = 1
            elif state == 1:
                if line.strip() == "":
                    state = 2
                else:
                    self._parse_header_line(line, response)
            elif state == 2:
                if line != "\n":
                    body += line
        
        response.with_body(body)
        return response
                
    def _parse_respone_line(self, request_line):
        response_tokens = shlex.split(request_line)
        return HttpResponse(response_tokens[1], response_tokens[2])
    
    def _parse_header_line(self, header_line, response):
        header_tokens = header_line.split(":")
        response.with_header(header_tokens[0].strip(), header_tokens[1].strip())