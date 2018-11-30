#!/usr/bin/env python
#
# Copyright 2016 Cisco Systems, Inc.
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

from argparse import ArgumentParser
import sys
if sys.version_info > (3,):
    from urllib.parse import urlparse
else:
    from urlparse import urlparse

from multiprocessing import Pool
import logging

from ydk.path import Repository
from ydk.filters import YFilter

from ydk.gnmi.providers import gNMIServiceProvider
from ydk.gnmi.services import gNMIService, gNMISubscription

from ydk.models.ydktest import openconfig_interfaces


def print_telemetry_data(s):
    print(s)

def get_local_repo_dir():
    import os
    path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(path, '../../../cpp/core/tests/models')
    return path

def build_int_config(provider):
    ifc = openconfig_interfaces.Interfaces()
    lo10 = ifc.Interface()
    lo10.name = 'Loopback10'
    lo10.config.name = 'Loopback10'
    lo10.config.description = 'Test'
    ifc.interface.append(lo10)
    ifc.yfilter = YFilter.replace

    gs = gNMIService()
    gs.set(provider, ifc)

def subscribe(args):
    func = args[0]
    device = args[1]
    mode = args[2]

    gnmi = gNMIService()
    repository = Repository(get_local_repo_dir())
    provider = gNMIServiceProvider(repo=repository,
                                      address=device.hostname,
                                      port=device.port,
                                      username=device.username,
                                      password=device.password)

    build_int_config(provider)

    inf = openconfig_interfaces.Interfaces()
    i = openconfig_interfaces.Interfaces.Interface()
    inf.interface.append(i)

    int_subscription = gNMISubscription()
    int_subscription.entity = inf
    int_subscription.subscription_mode = "SAMPLE"
    int_subscription.sample_interval = 20 * 1000000000
    int_subscription.suppress_redundant = False
    int_subscription.heartbeat_interval = 100 * 1000000000

    gnmi.subscribe(provider, int_subscription, 10, mode, 'JSON_IETF', func)


if __name__ == "__main__":
    """Execute main program."""
    parser = ArgumentParser()
    parser.add_argument("-v", "--verbose", help="print debugging messages",
                        action="store_true")
    parser.add_argument("device",
                        help="gNMI device (ssh://user:password@host:port)")
    parser.add_argument("-m", "--mode", help="Subscription mode. One of 'POLL', 'ONCE', 'STREAM'", dest='mode', default='ONCE')
    args = parser.parse_args()
    device = urlparse(args.device)

    # log debug messages if verbose argument specified
    if args.verbose:
        logger = logging.getLogger("ydk")
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(("%(asctime)s - %(name)s - "
                                      "%(levelname)s - %(message)s"))
        handler.setFormatter(formatter)
        logger.addHandler(handler)
 
    pool = Pool()
    pool.map(subscribe, [(print_telemetry_data, device, args.mode)])

