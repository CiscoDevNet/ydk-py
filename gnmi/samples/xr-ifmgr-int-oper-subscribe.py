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

usage: xr-ifmgr-int-oper-subscribe.py [[-h] | device [-v] [-m mode] [-ca file]

positional arguments:
  device - gNMI device with credentials (ssh://user:password@host:port)

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  print debugging messages
  -m, --mode     Subscription mode. One of 'POLL', 'ONCE', 'STREAM'
  -ca            File location for gNMI server certificate of authorization
"""

from argparse import ArgumentParser
from urlparse import urlparse
import datetime

from test_utils import enable_logging, print_entity

from ydk.path import Repository
from ydk.gnmi.providers import gNMIServiceProvider
from ydk.gnmi.services import gNMIService, gNMISubscription

from ydk.models.cisco_ios_xr import Cisco_IOS_XR_ifmgr_oper as ifoper
from ydk.types import Empty
from ydk.filters import YFilter

def gnmi_subscribe_callback(response):
    currentDT = datetime.datetime.now()
    print("===> Received subscribe response:")
    print(response)
    print("===> End of subscribe response - %s" % currentDT.strftime("%Y-%m-%d %H:%M:%S"))

def run_test(device, mode, ca, call_back):

    # Create gNMI Service Provider and gNMI Service
    repo = Repository("/home/ygorelik/ydk-gen/scripts/samples/repository/192.168.122.107")
    provider = gNMIServiceProvider(repo, address=device.hostname,
                                      port=device.port,
                                      username=device.username,
                                      password=device.password,
                                      server_certificate=ca)
    gs = gNMIService()

    """Build entity for interface operational data"""
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

    """Build subscription"""
    subscription = gNMISubscription()
    subscription.entity = ifc_oper_filter
    subscription.suppress_redundant = False;
    subscription.subscription_mode = "SAMPLE";
    subscription.sample_interval    = 3 * 1000000000;
    subscription.heartbeat_interval = 30 * 1000000000;

    """Send sunscribe request"""
    gs.subscribe(provider, subscription, 10, mode, "PROTO", call_back);

if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("-v", "--verbose", help="Print debugging messages", default=False, dest='verbose', action="store_true")
    parser.add_argument("device",
                        help="gNMI server credentials in format: ssh://<user>:<password>@<host-ip>:<port>)")
    parser.add_argument("-m", "--mode", help="Subscription mode. One of 'POLL', 'ONCE', 'STREAM'; default mode is 'ONCE'",
                        dest='mode', choices=['POLL', 'ONCE', 'STREAM'], default='ONCE')

    parser.add_argument("-ca", help="File location for gNMI server certificate of authorization. If not specified, it is assumed non-secure connecton", default='', dest='ca')

    args = parser.parse_args()
    device = urlparse(args.device)

    # log debug messages if verbose argument specified
    if args.verbose:
        import logging
        enable_logging(logging.DEBUG)

    run_test(device, args.mode, args.ca, gnmi_subscribe_callback)
