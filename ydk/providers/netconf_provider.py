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
import logging
from ._network_element import _NetworkElement
from .provider import ServiceProvider
from ._session_config import _SessionConfig
from ._ydk_types import _SessionTransportMode, _ServiceProtocolName


class NetconfServiceProvider(ServiceProvider):
    """ NCClient based Netconf ServiceProvider 
    
        Initialization parameter of NetconfServiceProvider
        
        kwargs:
            - address - The address of the netconf server
            - port  - The port to use default is 830
            - username - The name of the user
            - password - The password to use
            - protocol - one of either ssh or tcp    
    """

    def __init__(self, **kwargs):
        self.address = kwargs.get('address', '127.0.0.1')
        self.port = kwargs.get('port', 830)
        self.username = kwargs.get('username', 'admin')
        self.password = kwargs.get('password', 'admin')
        self.protocol = kwargs.get('protocol', 'ssh')

        if self.protocol == 'tcp':
            self.session_config = _SessionConfig(
                                                 _SessionTransportMode.TCP,
                                                 self.address,
                                                 self.port,
                                                 self.username,
                                                 self.password)
        else:
            self._session_config = _SessionConfig(
                                           _SessionTransportMode.SSH,
                                           self.address,
                                           self.port,
                                           self.username,
                                           self.password)

        self.ne = _NetworkElement(
                                  self._session_config,
                                  _ServiceProtocolName.NETCONF)

        netconf_sp_logger = logging.getLogger('ydk.providers.NetconfServiceProvider')
        self.ne.connect()
        netconf_sp_logger.info('NetconfServiceProvider connected to %s:%s using %s'
                               % (self.address, self.port, self.protocol))

        self.sp_instance = self.ne.sp_instance
        self.payload_log = self.ne.payload_log
        self.encode_format = self.ne.encode_format

    def close(self):
        """ Closes the netconf session """
        self.ne.disconnect()
