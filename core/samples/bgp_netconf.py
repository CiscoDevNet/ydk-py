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
from ydk.types import Empty
from ydk.providers import NetconfServiceProvider, CodecServiceProvider
from ydk.services import CRUDService, NetconfService, CodecService, Datastore
from ydk.models.openconfig import openconfig_bgp
from ydk.models.openconfig import openconfig_bgp_types
from ydk.models.openconfig.openconfig_routing_policy import RoutingPolicy

from _config_builder import _get_bgp_config, _get_routing_cfg, _get_bgp_routing_multiple_object



def bgp_run(netconf_service, session):
    # set up routing policy definition
    routing_policy = _get_routing_cfg()
    netconf_service.edit_config(session, Datastore.candidate, routing_policy)

    bgp_cfg = _get_bgp_config()
    # IPv4 Neighbor instance config done
    netconf_service.edit_config(session, Datastore.candidate, bgp_cfg)

    bgp_cfg_read = netconf_service.get_config(session, Datastore.candidate, bgp.Bgp())
    print(bgp_cfg_read)

    # IPv6 Neighbor instance config
    nbr_ipv6 = bgp.Bgp.Neighbors.Neighbor()
    nbr_ipv6.parent = bgp_cfg.neighbors
    nbr_ipv6.neighbor_address = '2001:db8:fff1::1'
    nbr_ipv6.config.neighbor_address = '2001:db8:fff1::1'
    nbr_ipv6.config.peer_as = 65002

    nbr_ipv6_afsf = nbr_ipv6.afi_safis.AfiSafi()
    nbr_ipv6_afsf.afi_safi_name = openconfig_bgp_types.Ipv6Unicast()
    nbr_ipv6_afsf.config.peer_as = 65002
    nbr_ipv6_afsf.config.afi_safi_name = openconfig_bgp_types.Ipv6Unicast()
    nbr_ipv6_afsf.config.enabled = True

    nbr_ipv6.afi_safis.afi_safi.append(nbr_ipv6_afsf)

    netconf_service.edit_config(session, Datastore.candidate, bgp_cfg)

    nbr_ipv6_filter = bgp.Bgp.Neighbors.Neighbor()
    nbr_ipv6_filter.neighbor_address = '2001:db8:fff1::1'

    nbr_ipv6_read = netconf_service.get_config(session, Datastore.candidate, bgp_cfg)

    print(nbr_ipv6_read)


def run_multiple_routing_bgp(netconf_service, session):
    crud = CRUDService()
    codec = CodecService()
    codec_provider = CodecServiceProvider()

    crud.delete(session, bgp())
    crud.delete(session, RoutingPolicy())

    multi_cfg = _get_bgp_routing_multiple_object()
    multi_payload_expected = codec.encode(codec_provider, multi_cfg)

    result = netconf_service.edit_config(session, Datastore.candidate, multi_cfg)
    assert 'ok' in result

    multi_filter = {'bgp':bgp(), 'routing-policy':RoutingPolicy()}
    multi_entity_read = netconf_service.get_config(session, Datastore.candidate, multi_filter)

    multi_payload_actual = codec.encode(codec_provider, multi_entity_read)

    assert multi_payload_expected == multi_payload_actual


def init_logging():
    import logging
    logger = logging.getLogger("ydk")
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(("%(asctime)s - %(name)s - "
                                  "%(levelname)s - %(message)s"))
    handler.setFormatter(formatter)
    logger.addHandler(handler)


if __name__ == "__main__":
    init_logging()
    provider = NetconfServiceProvider(address='localhost', username='admin', password='admin', protocol='ssh', port=1220)
    netconf_service = NetconfService()
    bgp_run(netconf_service, provider)
    # run_multiple_routing_bgp(netconf_service, provider)
    exit()
