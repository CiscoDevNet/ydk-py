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
# hello_ydk_gnmi.py
# Read all data for model Cisco-IOS-XR-shellutil-oper.yang and print system name and uptime.
#
import logging
from datetime import timedelta

# import providers, services and models
from ydk.path import Repository
from ydk.services import CRUDService
from ydk.gnmi.providers import gNMIServiceProvider
from ydk.models.cisco_ios_xr import Cisco_IOS_XR_shellutil_oper as xr_shellutil_oper

def enable_logging(level):
    log = logging.getLogger('ydk')
    log.setLevel(level)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
    handler.setFormatter(formatter)
    log.addHandler(handler)

if __name__ == "__main__":
    """Main execution path"""

    enable_logging(logging.INFO)
    
    # create NETCONF session
    repo = Repository('/home/ygorelik/.ydk/192.168.122.169_830')
    provider = gNMIServiceProvider(repo,
                                      address="192.168.122.169",
                                      port=57400,
                                      username="admin",
                                      password="admin")
    # create CRUD service
    crud = CRUDService()

    # create system time object
    system_time = xr_shellutil_oper.SystemTime()

    # read system time from device
    system_time = crud.read(provider, system_time)

    # print system uptime
    print("System '%s' uptime is "%system_time.uptime.host_name +
          str(timedelta(seconds=system_time.uptime.uptime)))

    exit()
