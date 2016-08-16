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
from ._ydk_types import _DEFAULT_SERVICE_TYPE, _DEFAULT_TRANSPORT_MODE


class _SessionConfig(object):

    '''
    SessionConfig contains the configuration that will be used
    for connecting to the network element.

    SessionConfig provides a means to configure session attributes
    prior to connecting to a NetworkElement.

    The SessionConfig object is required only if the defaults need to
    be overridden. Passing a null for the SessionConfig in the
    connect() call will result in a SSH connection between the application
    and the network element using default values. See specific setter APIs
    for the defaults for each attribute.
    '''

    def __init__(self, transport, hostname, port, username, password):
        '''
        Constructor

        Keyword argument:
        transport
            One of the options in SessionConfig.SessionTransportMode
            defaults to SessionConfig.SessionTransportMode.SSH
        hostname
           The hostname/ip address of the endpoint
        port
            The port to connect to on the endpoint
        username
           The username
        password
           The password used for connecting

        '''
        if transport is None:
            self.transportMode = _DEFAULT_TRANSPORT_MODE
        else:
            self.transportMode = transport

        if hostname is None:
            self.hostname = "localhost"
        else:
            self.hostname = hostname

        if port is None:
            self.port = "830"
        else:
            self.port = port

        self.username = username
        self.password = password

    def _set_transport_mode(self, transportMode):
        if transportMode is None:
            transportMode = _DEFAULT_TRANSPORT_MODE
        self._transportMode = transportMode

    def _get_transport_mode(self):
        return self._transportMode

    _doc_transport_mode = '''
    Transport type to be used for the session. If the value is None,
    the default transport type will be used. The default transport is
    SessionConfig.SessionTransportMode.SSH
    '''
    transportMode = property(
        _get_transport_mode,
        _set_transport_mode,
        None,
        _doc_transport_mode)

    def _set_service_type(self, serviceType):
        if serviceType is None:
            serviceType = _DEFAULT_SERVICE_TYPE
        self._serviceType = serviceType

    def _get_service_type(self):
        return self._serviceType

    _doc_service_type = '''
    Service type to be used for the session. If the value is None,
    the default service type will be used. The default transport is
    SessionConfig.SessionServiceType.NETCONF
    '''
    serviceType = property(
        _get_service_type,
        _set_service_type,
        None,
        _doc_service_type)
