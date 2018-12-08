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
Create configuration for model Cisco_IOS_XR_ifmgr_oper.

usage: xr-ifmgr-int-oper.py [-h] [-v] device

positional arguments:
  device - gNMI enabled device (ssh://user:password@host:port)

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  print debugging messages
"""

from argparse import ArgumentParser
from urlparse import urlparse

from test_utils import enable_logging, print_entity

from ydk.path import Repository, Codec
from ydk.gnmi.providers import gNMIServiceProvider
from ydk.gnmi.services import gNMIService
from ydk.services import CRUDService

from ydk.models.cisco_ios_xr import Cisco_IOS_XR_ifmgr_cfg as ifmgr
from ydk.models.cisco_ios_xr import Cisco_IOS_XR_ifmgr_oper as ifoper
from ydk.models.cisco_ios_xr import Cisco_IOS_XR_pfi_im_cmd_oper as pfioper
from ydk.types import Empty
from ydk.filters import YFilter

def run_test(provider):
    root = provider.get_session().get_root_schema()
    crud = CRUDService()
    
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

    reply = crud.update(provider, ifc_create)

    """Read interface operational data"""
    ifc_oper_filter = ifoper.InterfaceProperties()
    dn = ifoper.InterfaceProperties.DataNodes.DataNode()
    dn.data_node_name = '"0/RP0/CPU0"'
    ifc_oper_filter.data_nodes.data_node.append(dn)

    lview = ifoper.InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview()
    lview.locationview_name = '"0/RP0/CPU0"'
    dn.locationviews.locationview.append(lview)
    
    ifc = ifoper.InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces.Interface()
    ifc.interface_name = '"Loopback10"'
    ifc.state = YFilter.read
    lview.interfaces.interface.append(ifc)

    ifc_oper_data = crud.read(provider, ifc_oper_filter)
    if ifc_oper_data is not None:
        print('INTERFACE OPERATIONAL DATA:')
        print_entity(ifc_oper_data, root)

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
    provider = gNMIServiceProvider(repo, address=device.hostname,
                                      port=device.port,
                                      username=device.username,
                                      password=device.password)
    run_test(provider)

# End of script
