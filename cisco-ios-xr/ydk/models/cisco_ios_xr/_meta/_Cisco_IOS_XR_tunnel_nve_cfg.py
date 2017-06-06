


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'VxlanUdpPortEnumEnum' : _MetaInfoEnum('VxlanUdpPortEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_cfg',
        {
            'ietf-udp-port':'ietf_udp_port',
            'ivx-lan-udp-port':'ivx_lan_udp_port',
        }, 'Cisco-IOS-XR-tunnel-nve-cfg', _yang_ns._namespaces['Cisco-IOS-XR-tunnel-nve-cfg']),
    'OverlayEncapEnumEnum' : _MetaInfoEnum('OverlayEncapEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_cfg',
        {
            'vx-lan-encapsulation':'vx_lan_encapsulation',
            'soft-gre-encapsulation':'soft_gre_encapsulation',
        }, 'Cisco-IOS-XR-tunnel-nve-cfg', _yang_ns._namespaces['Cisco-IOS-XR-tunnel-nve-cfg']),
    'LoadBalanceEnumEnum' : _MetaInfoEnum('LoadBalanceEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_cfg',
        {
            'per-evi':'per_evi',
        }, 'Cisco-IOS-XR-tunnel-nve-cfg', _yang_ns._namespaces['Cisco-IOS-XR-tunnel-nve-cfg']),
    'UnknownUnicastFloodingEnumEnum' : _MetaInfoEnum('UnknownUnicastFloodingEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_cfg',
        {
            'suppress-uuf':'suppress_uuf',
        }, 'Cisco-IOS-XR-tunnel-nve-cfg', _yang_ns._namespaces['Cisco-IOS-XR-tunnel-nve-cfg']),
    'HostReachProtocolEnum' : _MetaInfoEnum('HostReachProtocolEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_cfg',
        {
            'bgp':'bgp',
        }, 'Cisco-IOS-XR-tunnel-nve-cfg', _yang_ns._namespaces['Cisco-IOS-XR-tunnel-nve-cfg']),
}
