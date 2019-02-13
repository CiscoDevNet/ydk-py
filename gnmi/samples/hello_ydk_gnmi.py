#!/usr/bin/env python
# =======================================================================
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
# ========================================================================
"""
hello_ydk_gnmi.py
Read all data for model Cisco-IOS-XR-shellutil-oper.yang and print system name and uptime.

Usage: hello_ydk_gnmi.py [-h] [-v] device repo
Positional arguments:
  device      gNMI enabled device (ssh://user:password@host:port)
  repo        yang model repository location - full path to repository directory
Optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  print debugging messages
Example:
  hello_ydk_gnmi.py -v ssh://root:Cisco123!@172.27.150.154:57800 /home/yan/.ydk/172.27.150.154_830
"""
import logging
from datetime import timedelta
from argparse import ArgumentParser
import sys
if sys.version_info > (3,):
    from urllib.parse import urlparse
else:
    from urlparse import urlparse

from test_utils import enable_logging

# import providers, services and models
from ydk.path import Repository
from ydk.services import CRUDService
from ydk.gnmi.providers import gNMIServiceProvider

from ydk.models.cisco_ios_xr import Cisco_IOS_XR_shellutil_oper as xr_shellutil_oper

if __name__ == "__main__":
    """Execute main program."""
    parser = ArgumentParser()
    parser.add_argument("-v", "--verbose", help="print debugging messages",
                        action="store_true")
    parser.add_argument("device",
                        help="gNMI device (ssh://user:password@host:port)")
    parser.add_argument("repo",
                        help="yang model repository location - full path to repository directory")

    args = parser.parse_args()
    device = urlparse(args.device)
    repo_path = args.repo

    # log debug messages if verbose argument specified
    if args.verbose:
        enable_logging(logging.INFO)

    # create gNMI session
    repo = Repository(repo_path)
    provider = gNMIServiceProvider(repo,
                                   address=device.hostname,
                                   port=device.port,
                                   username=device.username,
                                   password=device.password)
    # create CRUD service
    crud = CRUDService()

    # create system time object
    system_time = xr_shellutil_oper.SystemTime()

    # read system time from device
    system_time = crud.read(provider, system_time)

    # print system name and uptime
    print("System '%s' uptime is "%system_time.uptime.host_name +
          str(timedelta(seconds=system_time.uptime.uptime)))
