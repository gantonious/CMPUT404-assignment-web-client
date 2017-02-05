import re
import urlparse
from httprequest import HttpRequest

class HostBasedRequest(HttpRequest):
    def __init__(self, method, url):
        self.parsed_url = urlparse.urlparse(url)

        HttpRequest.__init__(self, method, self.parsed_url.path)
        self.with_header("Host", self.parsed_url.netloc)

    def host_address(self):
        return self.parsed_url.hostname

    def host_port(self):
        return self.parsed_url.port or 80

class GetRequest(HostBasedRequest):
    def __init__(self, url):
        HostBasedRequest.__init__(self, "GET", url)

class PostRequest(HostBasedRequest):
    def __init__(self, url):
        HostBasedRequest.__init__(self, "POST", url)
        self.with_header("Content-Length", 0)