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

"""restconf_session.py
RestconfSession Python wrapper.
"""

from ydk.ext.types import EncodingFormat as _EncodingFormat
from ydk.ext.path import RestconfSession as _RestconfSession


class RestconfSession(_RestconfSession):
    """ Python wrapper for RestconfSession.
    """

    def __init__(self, repo, address, username, password,
                       port=80, encoding=_EncodingFormat.JSON,
                       config_url_root="/data", state_url_root="/data"):
        super(RestconfSession, self).__init__(repo, address, username, password,
                                              port, encoding, config_url_root,
                                              state_url_root)

    def get_root_schema(self):
        return super(RestconfSession, self).get_root_schema()

    def invoke(self, rpc):
        return super(RestconfSession, self).invoke(rpc)
