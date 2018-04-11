#!/usr/bin/env python
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
""" bgp_xr_opendaylight.py

Sample app for odl.
"""
import os
import sys
from argparse import ArgumentParser
if sys.version_info > (3,):
    from urllib.parse import urlparse
else:
    from urlparse import urlparse

from ydk.types import Empty
from ydk.services import CRUDService
from ydk.providers import OpenDaylightServiceProvider
from ydk.errors import YError
from ydk.types import EncodingFormat
from ydk.path import Repository
from ydk.models.cisco_ios_xr import Cisco_IOS_XR_ipv4_bgp_cfg as xr_bgp
from ydk.models.cisco_ios_xr import Cisco_IOS_XR_ipv4_bgp_datatypes as xr_bgp_types

from session_mgr import init_logging

"""
<?xml version="1.0" encoding="UTF-8"?>
<bgp xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ipv4-bgp-cfg">
   <instance>
      <instance-name>test</instance-name>
      <instance-as>
         <as>65001</as>
         <four-byte-as>
            <as>65001</as>
            <bgp-running />
            <default-vrf>
               <bgp-entity>
                  <neighbor-groups>
                     <neighbor-group>
                        <neighbor-group-name>IBGP</neighbor-group-name>
                        <create />
                        <update-source-interface>Loopback0</update-source-interface>
                        <neighbor-group-afs>
                           <neighbor-group-af>
                              <af-name>ipv4-unicast</af-name>
                              <activate />
                           </neighbor-group-af>
                        </neighbor-group-afs>
                        <remote-as>
                           <as-xx>0</as-xx>
                           <as-yy>65001</as-yy>
                        </remote-as>
                     </neighbor-group>
                  </neighbor-groups>
                  <neighbors>
                     <neighbor>
                        <neighbor-address>172.16.255.2</neighbor-address>
                        <neighbor-group-add-member>IBGP</neighbor-group-add-member>
                     </neighbor>
                  </neighbors>
               </bgp-entity>
               <global>
                  <global-afs>
                     <global-af>
                        <af-name>ipv4-unicast</af-name>
                        <enable />
                     </global-af>
                  </global-afs>
               </global>
            </default-vrf>
         </four-byte-as>
      </instance-as>
   </instance>
</bgp>
"""

def odl_run(crud_service, session):

    bgp = xr_bgp.Bgp()
    instance = bgp.Instance()
    bgp.instance.append(instance)
    instance.instance_name = 'test'
    instance_as = xr_bgp.Bgp.Instance.InstanceAs()
    instance_as.as_ = 65001
    instance.instance_as.append(instance_as)
    four_byte_as = xr_bgp.Bgp.Instance.InstanceAs.FourByteAs()
    four_byte_as.as_ = 65001
    four_byte_as.bgp_running = Empty()
    instance_as.four_byte_as.append(four_byte_as)

    # global address family
    global_af = four_byte_as.DefaultVrf.Global_.GlobalAfs.GlobalAf()
    global_af.af_name = xr_bgp_types.BgpAddressFamilyEnum.ipv4_unicast
    global_af.enable = Empty()
    four_byte_as.default_vrf.global_.global_afs.global_af.append(global_af)

    # configure IBGP neighbor group
    neighbor_group = four_byte_as.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup()
    neighbor_group.neighbor_group_name = 'IBGP'
    neighbor_group.create = Empty()
    # remote AS
    neighbor_group.remote_as.as_xx = 0
    neighbor_group.remote_as.as_yy = 65001
    neighbor_group.update_source_interface = 'Loopback0'
    four_byte_as.default_vrf.bgp_entity.neighbor_groups.neighbor_group.append(neighbor_group)
    # ipv4 unicast
    neighbor_group_af = neighbor_group.NeighborGroupAfs.NeighborGroupAf()
    neighbor_group_af.af_name = xr_bgp_types.BgpAddressFamilyEnum.ipv4_unicast
    neighbor_group_af.activate = Empty()
    neighbor_group.neighbor_group_afs.neighbor_group_af.append(neighbor_group_af)

    # configure IBGP neighbor
    neighbor = four_byte_as.DefaultVrf.BgpEntity.Neighbors.Neighbor()
    neighbor.neighbor_address = '172.16.255.2'
    neighbor.neighbor_group_add_member = 'IBGP'
    four_byte_as.default_vrf.bgp_entity.neighbors.neighbor.append(neighbor)

    crud_service.create(provider.get_node_provider('xr'), bgp)


if __name__ == "__main__":
    init_logging()
    repository_path = os.path.join(os.path.expanduser('~'),
                                   'Cisco',
                                   'odl',
                                   'distribution-karaf-0.5.2-Boron-SR2',
                                   'cache',
                                   'schema')
    if not os.path.exists(repository_path):
        os.makedirs(repository_path)
    repository = Repository(repository_path)

    parser = ArgumentParser()
    parser.add_argument("-v", "--verbose", help="print debugging messages",
                        action="store_true")
    parser.add_argument("device",
                        help="NETCONF device (ssh://user:password@host:port)")
    args = parser.parse_args()
    device = urlparse(args.device)

    provider = OpenDaylightServiceProvider(repository,
                                           device.hostname,
                                           device.username,
                                           device.password,
                                           device.port,
                                           EncodingFormat.XML)
    crud_service = CRUDService()
    odl_run(crud_service, provider)
    exit()
