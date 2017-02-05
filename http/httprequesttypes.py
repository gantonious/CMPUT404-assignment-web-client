import re
from httprequest import HttpRequest

class HostBasedRequest(HttpRequest):
    def __init__(self, method, url):
        host = self.extract_host_from_url(url)
        path = self.extract_path_from_url(url)

        HttpRequest.__init__(self, method, path)
        self.with_header("Host", host)

    def host_address(self):
        host_address = self.header("Host")

        if ":" in host_address:
            return host_address.split(":")[0]

        return host_address

    def host_port(self):
        host_address = self.header("Host")

        if ":" in host_address:
            return int(host_address.split(":")[1])

        return 80
    
    def extract_url_without_protocol(self, url):
        http_protocol_pattern = "https*:\/\/"
        return re.sub(http_protocol_pattern, "", url)

    def extract_host_from_url(self, url):
        pure_url = self.extract_url_without_protocol(url)
        
        if "/" in pure_url:
            return pure_url.split("/")[0]

        return pure_url

    def extract_path_from_url(self, url):
        pure_url = self.extract_url_without_protocol(url)
        
        if "/" in pure_url:
            index_of_slash = pure_url.index("/")
            return pure_url[index_of_slash:]
            
        return "/"

class GetRequest(HostBasedRequest):
    def __init__(self, url):
        HostBasedRequest.__init__(self, "GET", url)

class PostRequest(HostBasedRequest):
    def __init__(self, url):
        HostBasedRequest.__init__(self, "POST", url)