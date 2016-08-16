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
from enum import Enum


#
#  * Transport mode to be used for a session.
#  *
#  *  SSH:    Secure Shell
#  *  TLS:    Secured TLS socket
#  *  TIPC:   TIPC socket
#  *  TCP:    Plain Socket
class _SessionTransportMode(Enum):
    SSH = 1
    TLS = 2
    TIPC = 3
    TCP = 4


#
#      * Service Protocol Type to be used for a session.
#      *
#
class _ServiceProtocolName(Enum):
    NETCONF = 1
    ONEP = 2
    RESTCONF = 3


class _Encoding_Format(Enum):
    XML = 1
    JSON = 2


#
#      * Default transport mode is SSH in production environment.
#
_DEFAULT_TRANSPORT_MODE = _SessionTransportMode.SSH


#
#      * Default Service type is NETCONF in production environment.
#
_DEFAULT_SERVICE_TYPE = _ServiceProtocolName.NETCONF
_DEFAULT_ENCODING_FORMAT = _Encoding_Format.XML
_DEFAULT_NC_PORT = 830
