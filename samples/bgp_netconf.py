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



from ydk.types import Empty
from ydk.providers import NetconfServiceProvider
from ydk.services import NetconfService

from samples.session_mgr import init_logging
from ydk.models.bgp import bgp
from ydk.models.bgp.bgp_types import Ipv4Unicast_Identity
from ydk.models.bgp.bgp_types import Ipv6Unicast_Identity
from ydk.models.routing.routing_policy import RoutingPolicy
from ydk.errors import YPYError
from ydk.services import Datastore



# <bgp xmlns="http://openconfig.net/yang/bgp">
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
# </bgp>



def bgp_run(netconf_service, session):
    bgp_cfg = bgp.Bgp()

    # set up routing policy definition
    routing_policy = RoutingPolicy()

    pass_all_policy_defn = RoutingPolicy.PolicyDefinitions.PolicyDefinition()
    pass_all_policy_defn.name = 'PASS-ALL'

    routing_policy.policy_definitions.policy_definition.append(pass_all_policy_defn)
    pass_all_policy_defn._parent = routing_policy.policy_definitions

    netconf_service.edit_config(session, Datastore.candidate, routing_policy)

    bgp_cfg.global_.config.as_ = 65001

    ipv4_afsf = bgp_cfg.global_.afi_safis.AfiSafi()
    ipv4_afsf.afi_safi_name = 'ipv4-unicast'
    ipv4_afsf.config.afi_safi_name = 'ipv4-unicast'
    ipv4_afsf.config.enabled = True

    ipv6_afsf = bgp_cfg.global_.afi_safis.AfiSafi()
    ipv6_afsf.afi_safi_name = 'ipv6-unicast'
    ipv6_afsf.config.afi_safi_name = 'ipv6-unicast'
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
    nbr_ipv4_afsf.afi_safi_name = 'ipv4-unicast'
    nbr_ipv4_afsf.config.peer_as = 65002
    nbr_ipv4_afsf.config.afi_safi_name = 'ipv4-unicast'
    nbr_ipv4_afsf.config.enabled = True

    # Create afi-safi policy instances
    nbr_ipv4.afi_safis.afi_safi.append(nbr_ipv4_afsf)

    bgp_cfg.neighbors.neighbor.append(nbr_ipv4)
    nbr_ipv4.parent = bgp_cfg.neighbors

    # IPv4 Neighbor instance config done
    netconf_service.edit_config(session, Datastore.candidate, bgp_cfg)

    bgp_cfg_read = netconf_service.get_config(session, Datastore.candidate, bgp.Bgp())
    print bgp_cfg_read

    # IPv6 Neighbor instance config
    nbr_ipv6 = bgp.Bgp.Neighbors.Neighbor()
    nbr_ipv6.parent = bgp_cfg.neighbors
    nbr_ipv6.neighbor_address = '2001:db8:fff1::1'
    nbr_ipv6.config.neighbor_address = '2001:db8:fff1::1'
    nbr_ipv6.config.peer_as = 65002

    nbr_ipv6_afsf = nbr_ipv6.afi_safis.AfiSafi()
    nbr_ipv6_afsf.afi_safi_name = 'ipv6-unicast'
    nbr_ipv6_afsf.config.peer_as = 65002
    nbr_ipv6_afsf.config.afi_safi_name = 'ipv6-unicast'
    nbr_ipv6_afsf.config.enabled = True

    nbr_ipv6.afi_safis.afi_safi.append(nbr_ipv6_afsf)

    netconf_service.edit_config(session, Datastore.candidate, bgp_cfg)

    nbr_ipv6_filter = bgp.Bgp.Neighbors.Neighbor()
    nbr_ipv6_filter.neighbor_address = '2001:db8:fff1::1'

    nbr_ipv6_read = netconf_service.get_config(session, Datastore.candidate, bgp_cfg)

    print nbr_ipv6_read


if __name__ == "__main__":
    init_logging()
    provider = NetconfServiceProvider(address='127.0.0.1', username='admin', password='admin', protocol='ssh', port=12022)
    netconf_service = NetconfService()
    bgp_run(netconf_service, provider)
    exit()
