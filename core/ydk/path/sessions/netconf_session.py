#  ----------------------------------------------------------------
# Copyright 2017 Cisco Systems
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

"""netconf_session.py
NetconfSession Python wrapper.
"""

from ydk.ext.path import NetconfSession as _NetconfSession


class NetconfSession(_NetconfSession):
    """ Python wrapper for NetconfSession
    """

    def __init__(self, address, username, password, port=830, protocol="ssh",
                       on_demand=True, common_cache=False, timeout=-1, repo=None):
        if repo is None:
            super(NetconfSession, self).__init__(address, username, password,
                                                 port, protocol, on_demand,
                                                 common_cache, timeout)
        else:
            super(NetconfSession, self).__init__(repo, address, username,
                                                 password, port, protocol,
                                                 on_demand, timeout)

    def get_root_schema(self):
        return super(NetconfSession, self).get_root_schema()

    def invoke(self, rpc):
        return super(NetconfSession, self).invoke(rpc)

    def get_capabilities(self):
        return super(NetconfSession, self).get_capabilities()