#  ----------------------------------------------------------------
# Copyright 2018 Cisco Systems
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------

"""gnmi_provider.py
gNMIServiceProvider Python wrapper.
"""

from ydk_gnmi_.providers import gNMIServiceProvider as _gNMIServiceProvider


class gNMIServiceProvider(_gNMIServiceProvider):
    """ Python wrapper for gNMIServiceProvider
    """

    def __init__(self, repo, address, port, username, password,
                       server_certificate=None, private_key=None):

        if port is None:
            port = 57400
        if server_certificate is None:
            server_certificate = ""
        if private_key is None:
            private_key = ""

        super(gNMIServiceProvider, self).__init__(repo, address, port,
                                                  username, password,
                                                  server_certificate, private_key)

    def get_encoding(self):
        return super(gNMIServiceProvider, self).get_encoding()

    def get_session(self):
        return super(gNMIServiceProvider, self).get_session()

    def get_capabilities(self):
        return super(gNMIServiceProvider, self).get_capabilities()
