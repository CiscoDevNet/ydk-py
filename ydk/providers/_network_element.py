#  ----------------------------------------------------------------
# Copyright 2016 Cisco Systems
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

""" providers.py 
 
   Service Providers module. Current implementation supports the NetconfServiceProvider which
   uses ncclient (a Netconf client library) to provide CRUD services.
   
"""
from ._provider_plugin import _NCClientSPPlugin
from ._ydk_types import _DEFAULT_ENCODING_FORMAT, _DEFAULT_NC_PORT


class _NetworkElement(object):

    def __init__(self, session_config, service_protocol_type, encode_format=None, port=None):

        self.session_config = session_config

        if service_protocol_type is None:
            self.service_protocol_type = self.DEFAULT_SERVICE_TYPE
        else:
            self.service_protocol_type = service_protocol_type
        if encode_format == None:
            self.encode_format = _DEFAULT_ENCODING_FORMAT
        else:
            self.encode_format = encode_format
        if port is None:
            self.port = _DEFAULT_NC_PORT
        else:
            self.port = port

        self.sp_instance = None

    def connect(self):
        netconf_client = _NCClientSPPlugin('Netconf Protocol')
        self.sp_instance = netconf_client
        netconf_client._connect(self.session_config, self.port)
        return True

    def disconnect(self):
        self.sp_instance._nc_manager.close_session()
        return True

