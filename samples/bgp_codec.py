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
#  bgp_codec.py Sample program illustrating use of codec service for
#  ydk.models.bgp.bgp.py which in turn is derived from the
#  open-config bgp yang module.
#


from ydk.providers import CodecServiceProvider
from ydk.services import CodecService

from samples.session_mgr import init_logging
from ydk.models.bgp import bgp


def bgp_run(codec_service, provider):
    bgp_cfg = bgp.Bgp()

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
    print codec_service.encode(provider, bgp_cfg)
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
    bgp_payload = codec_service.encode(provider, bgp_cfg)
    bgp_entity = codec_service.decode(provider, bgp_payload)
    print 'Encoded payload:\n', bgp_payload, \
            '\nRe-encode the decoded payload:\n', codec_service.encode(provider, bgp_entity)
    assert bgp_payload == codec_service.encode(provider, bgp_entity)


if __name__ == "__main__":
    init_logging()
    provider = CodecServiceProvider(type='xml')
    codec_service = CodecService()
    bgp_run(codec_service, provider)
    exit()
