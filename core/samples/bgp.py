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


#  ----------------------------------------------------------------
#  bgp.py Sample program illustrating use of generated api
#  ydk.models.bgp.bgp.py which inturn is derived from the
#  open-config bgp yang module.
#



from __future__ import print_function
from __future__ import absolute_import
from ydk.types import Empty
from ydk.services import CRUDService
import logging

from session_mgr import establish_session, init_logging
from ydk.models.openconfig import openconfig_bgp
from ydk.models.openconfig import openconfig_bgp_types
from ydk.models.openconfig.openconfig_routing_policy import RoutingPolicy
from ydk.errors import YError




#<bgp xmlns="http://openconfig.net/yang/bgp">
#  <global>
#    <config>
#      <as>65172</as>
#    </config>
#    <afi-safi>
#      <afi-safi>
#        <afi-safi-name>l3vpn-ipv4-unicast</afi-safi-name>
#        <config>
#          <afi-safi-name>l3vpn-ipv4-unicast</afi-safi-name>
#          <enabled>true</enabled>
#        </config>
#      </afi-safi>
#    </afi-safis>
#  </global>
#  <neighbors>
#    <neighbor>
#      <neighbor-address>172.16.255.2</neighbor-address>
#      <config>
#        <neighbor-address>172.16.255.2</neighbor-address>
#        <peer-as>65172</peer-as>
#      </config>
#      <afi-safis>
#        <afi-safi>
#          <afi-safi-name>l3vpn-ipv4-unicast</afi-safi-name>
#          <config>
#            <afi-safi-name>l3vpn-ipv4-unicast</afi-safi-name>
#            <enabled>true</enabled>
#          </config>
#        </afi-safi>
#      </afi-safis>
#    </neighbor>
#  </neighbors>
#</bgp>



def bgp_run(crud_service, session):

    # Global config
    bgp_cfg = openconfig_bgp.Bgp()

    try:
        crud_service.delete(session, bgp_cfg)
    except Exception:
        print('BGP config does not exist!')

    #set up routing policy definition
    routing_policy = RoutingPolicy()

    #first delete
    try:
        crud_service.delete(session, routing_policy)
    except YError:
        print('Routing policy does not exist!')

    pass_all_policy_defn = RoutingPolicy.PolicyDefinitions.PolicyDefinition()
    pass_all_policy_defn.name = 'PASS-ALL'


    routing_policy.policy_definitions.policy_definition.append(pass_all_policy_defn)
    pass_all_policy_defn.parent = routing_policy.policy_definitions


    bgp_cfg.global_.config.as_ = 65001

    ipv4_afsf = bgp_cfg.global_.afi_safis.AfiSafi()
    ipv4_afsf.afi_safi_name = openconfig_bgp_types.Ipv4Unicast()
    ipv4_afsf.config.afi_safi_name = openconfig_bgp_types.Ipv4Unicast()
    ipv4_afsf.config.enabled = True

    ipv6_afsf = bgp_cfg.global_.afi_safis.AfiSafi()
    ipv6_afsf.afi_safi_name = openconfig_bgp_types.Ipv6Unicast()
    ipv6_afsf.config.afi_safi_name = openconfig_bgp_types.Ipv6Unicast()
    ipv6_afsf.config.enabled = True

    bgp_cfg.global_.afi_safis.afi_safi.append(ipv4_afsf)
    bgp_cfg.global_.afi_safis.afi_safi.append(ipv6_afsf)
    # Global config done

    # IPv4 Neighbor instance config
    nbr_ipv4 = bgp_cfg.neighbors.Neighbor()
    nbr_ipv4.neighbor_address = '192.168.1.1'
    nbr_ipv4.config.neighbor_address = '192.168.1.1'
    nbr_ipv4.config.peer_as = 65002

    nbr_ipv4_afsf = nbr_ipv4.afi_safis.AfiSafi()
    nbr_ipv4_afsf.afi_safi_name = openconfig_bgp_types.Ipv4Unicast()
    nbr_ipv4_afsf.config.peer_as = 65002
    nbr_ipv4_afsf.config.afi_safi_name = openconfig_bgp_types.Ipv4Unicast()
    nbr_ipv4_afsf.config.enabled = True

    # Create afi-safi policy instances
    nbr_ipv4_afsf.apply_policy.config.import_policy.append('PASS-ALL')

    nbr_ipv4_afsf.apply_policy.config.export_policy.append('PASS-ALL')

    nbr_ipv4.afi_safis.afi_safi.append(nbr_ipv4_afsf)


    bgp_cfg.neighbors.neighbor.append(nbr_ipv4)
    nbr_ipv4.parent = bgp_cfg.neighbors

    # IPv4 Neighbor instance config done

    crud_service.create(session, bgp_cfg)
#    crud_service.create(session, routing_policy)

    bgp_cfg_read = crud_service.read(session, bgp.Bgp())



    #crud on just the neighbor

    # IPv6 Neighbor instance config
    nbr_ipv6 = bgp.Bgp.Neighbors.Neighbor()
    #nbr_ipv6.parent = bgp_cfg.neighbors
    nbr_ipv6.neighbor_address = '2001:db8:fff1::1'
    nbr_ipv6.config.neighbor_address = '2001:db8:fff1::1'
    nbr_ipv6.config.peer_as = 65002

    nbr_ipv6_afsf = nbr_ipv6.afi_safis.AfiSafi()
    nbr_ipv6_afsf.afi_safi_name = openconfig_bgp_types.Ipv6Unicast()
    nbr_ipv6_afsf.config.peer_as = 65002
    nbr_ipv6_afsf.config.afi_safi_name = openconfig_bgp_types.Ipv6Unicast()
    nbr_ipv6_afsf.config.enabled = True

    # Create afi-safi policy instances
    nbr_ipv6_afsf.apply_policy.config.import_policy.append('PASS-ALL')

    nbr_ipv6_afsf.apply_policy.config.export_policy.append('PASS-ALL')

    nbr_ipv6.afi_safis.afi_safi.append(nbr_ipv6_afsf)

    crud_service.create(session,nbr_ipv6)

    #now delete nbr_ipv4
    crud_service.delete(session, nbr_ipv4)

    nbr_ipv6_filter = bgp.Bgp.Neighbors.Neighbor()
    nbr_ipv6_filter.neighbor_address = '2001:db8:fff1::1'


    nbr_ipv6_read = crud_service.read(session, nbr_ipv6_filter)


    # help(nbr_ipv6_read)
    print(nbr_ipv6_read)

    #crud_service.read(session,bgp_cfg1)


if __name__ == "__main__":
    init_logging()
    provider = establish_session()
    crud_service = CRUDService()
    bgp_run(crud_service, provider)
    exit()
