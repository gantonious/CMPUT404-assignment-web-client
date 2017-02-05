# Copyright 2017 George Antonious
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

import re
import urlparse
from httprequest import HttpRequest

class HostBasedRequest(HttpRequest):
    def __init__(self, method, url):
        self.parsed_url = urlparse.urlparse(url)

        HttpRequest.__init__(self, method, self.parsed_url.path or "/")
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