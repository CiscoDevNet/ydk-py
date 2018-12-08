#!/usr/bin/env python
#
# Copyright 2018 Cisco Systems, Inc.
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
#

"""
Create configuration for model Cisco_IOS_XR_ifmgr_cfg.

usage: xr-ifmgr-int.py [-h] [-v] device

positional arguments:
  device - gNMI enabled device (ssh://user:password@host:port)

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  print debugging messages
"""

from argparse import ArgumentParser
from urlparse import urlparse

from test_utils import enable_logging, print_entity

from ydk.filters import YFilter
from ydk.services import CRUDService
from ydk.path import Repository, Codec

from ydk.gnmi.providers import gNMIServiceProvider
from ydk.gnmi.services import gNMIService

from ydk.models.cisco_ios_xr import Cisco_IOS_XR_ifmgr_cfg as ifmgr
from ydk.types import Empty

def run_test(provider):
    root = provider.get_session().get_root_schema()
    service = gNMIService()
    
    """Create interface configuration"""
    ifc = ifmgr.InterfaceConfigurations.InterfaceConfiguration()
    ifc.active = 'act'
    ifc.interface_name = 'Loopback10'
    ifc.description = 'Test interface'
    ifc.interface_virtual = Empty()

    ip_address = ifmgr.InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Addresses.Primary()
    ip_address.address = '172.16.255.1'
    ip_address.netmask = '255.255.255.255'
    ifc.ipv4_network.addresses.primary = ip_address

    ifc_create = ifmgr.InterfaceConfigurations()
    ifc_create.interface_configuration.append(ifc)
    ifc_create.yfilter = YFilter.update

    reply = service.set(provider, ifc_create)

    """Read interface configuration"""
    ifc_filter = ifmgr.InterfaceConfigurations()
    ifc = ifmgr.InterfaceConfigurations.InterfaceConfiguration()
    ifc.active = '"act"'
    ifc.interface_name = '"Loopback10"'
    ifc_filter.interface_configuration.append(ifc)

    ifc_read = service.get(provider, ifc_filter)
    if ifc_read is not None:
        print_entity(ifc_read, root)

        """Need to fix bug in the XR bundle: missing directory _yang in distribution:
           RuntimeError: YIllegalStateError: Could not create repository in: /usr/local/lib/python2.7/dist-packages/ydk/models/cisco_ios_xr/_yang
        from ydk.services import CodecService
        from ydk.providers import CodecServiceProvider
        codec_service = CodecService()
        codec_provider = CodecServiceProvider(type='json')
        payload = codec_service.encode(codec_provider, ifc_read)
        print('CREATED INTERFACE CONFIGURATION:')
        print(payload)
        """

    """Delete interface configuration"""
    ifc_delete = ifmgr.InterfaceConfigurations()
    ifc = ifmgr.InterfaceConfigurations.InterfaceConfiguration()
    ifc.active = '"act"'
    ifc.interface_name = '"Loopback10"'
    ifc_delete.interface_configuration.append(ifc)
    ifc_delete.yfilter = YFilter.delete
    reply = service.set(provider, ifc_delete)

if __name__ == "__main__":

    """Execute main program."""
    parser = ArgumentParser()
    parser.add_argument("-v", "--verbose", help="print debugging messages",
                        action="store_true")
    parser.add_argument("device",
                        help="NETCONF device (ssh://user:password@host:port)")
    args = parser.parse_args()
    device = urlparse(args.device)

    # log debug messages if verbose argument specified
    if args.verbose:
        import logging
        enable_logging(logging.DEBUG)

    # create gNMI service provider
    repo = Repository("/home/ygorelik/ydk-gen/scripts/samples/repository/192.168.122.107")
    provider = gNMIServiceProvider(repo=repo,
                                   address=device.hostname,
                                   port=device.port,
                                   username=device.username,
                                   password=device.password)
    run_test(provider)

# End of script
